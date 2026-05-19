import glob
import json
import os

from jsonschema import Draft7Validator, SchemaError
from setuptools import Command
from tabulate import tabulate


DESCRIPTION_MD = (
    "Metadata in the depositar Data Package are expressed in a "
    "`datapackage.json` file. It follows the "
    "[Data Package](https://datapackage.org/standard/data-package/) "
    "specifications and includes generic **Data Package properties** "
    "and specific **depositar DP properties**. Properties indicated "
    "with `*` are required (i.e. cannot be empty).\n\n"
)


def get_constraints_from_ref(ref_data):
    constraints = []

    patterns = [f"`{item.get('pattern')}`" for item in ref_data if "pattern" in item]
    enum_values = [f"`{item.get('const')}`" for item in ref_data if "const" in item]
    if patterns:
        constraints.append(f"patterns: {', '.join(patterns)}")
    if enum_values:
        constraints.append(f"enum: {', '.join(enum_values)}")

    return constraints


def get_properties_data(schema_data):
    markdown_content = ""

    # Main properties
    main_props = schema_data["allOf"][1]["properties"]
    required_props = schema_data["allOf"][1].get("required", [])

    for prop_name, prop_details in main_props.items():
        is_nested_table = False

        # If the main property has nested properties (shown as a table)
        if "items" in prop_details and (
            "properties" in prop_details["items"].get("oneOf", [{}])[0]
            or "properties" in prop_details["items"]
        ):
            is_nested_table = True

            # Build table rows for the nested properties
            table_rows = []

            if "oneOf" in prop_details["items"]:
                nested_props = prop_details["items"]["oneOf"][0]["properties"]
                nested_required = prop_details["items"]["oneOf"][0].get("required", [])
            else:
                nested_props = prop_details["items"]["properties"]
                nested_required = prop_details["items"].get("required", [])

            for nested_name, nested_details in nested_props.items():
                name_display = nested_name + (
                    " *" if nested_name in nested_required else ""
                )
                type_display = (
                    f"`{nested_details.pop('type', '')}`"
                    if "type" in nested_details
                    else ""
                )

                table_row = {
                    "Name": name_display,
                    "Description": nested_details.pop("description", ""),
                    "Type": type_display,
                    "Example": nested_details.pop("example", ""),
                }

                constraints = []
                for key, value in nested_details.items():
                    if key == "enum":
                        constraints.append(f"{key}: {', '.join([f'`{v}`' for v in value])}")
                    elif key == "items" and "enum" in value:
                        constraints.append(f"enum: {', '.join([f'`{v}`' for v in value['enum']])}")
                    else:
                        constraints.append(f"{key}: `{value}`")
                table_row.update({"Constraints": ", ".join(constraints)})

                table_rows.append(table_row)

            # [MD] Write the basic information for the main property
            name_display = prop_name + (" *" if prop_name in required_props else "")
            markdown_content += f"## {name_display}\n\n"
            markdown_content += f"- **Description**: {prop_details.get('description', '')}\n"
            if prop_details.get("type"):
                markdown_content += f"- **Type**: `{prop_details.get('type', '')}`\n"
            if prop_details.get("example"):
                markdown_content += f"- **Example**: `{prop_details.get('example', '')}`\n"
            markdown_content += "\n"

            # [MD] Write table rows for the nested properties
            markdown_content += tabulate(table_rows, headers="keys", tablefmt="github")
            markdown_content += "\n\n"

        # For other properties without nested properties (shown as a list)
        if not is_nested_table:
            constraints = []

            if "$ref" in prop_details:
                ref_details = prop_details.pop("$ref")
                ref_path = ref_details.split("/")[-1]
                if "$defs" in schema_data and ref_path in schema_data["$defs"]:
                    ref_data = schema_data["$defs"][ref_path].get("anyOf")
                    if ref_data:
                        constraints.extend(get_constraints_from_ref(ref_data))

            if "items" in prop_details:
                item_details = prop_details.pop("items", {})
                for key, value in item_details.items():
                    if key == "enum":
                        constraints.append(f"{key}: {', '.join([f'`{v}`' for v in value])}")
                    if key == "$ref":
                        ref_path = value.split("/")[-1]
                        if "$defs" in schema_data and ref_path in schema_data["$defs"]:
                            ref_data = schema_data["$defs"][ref_path].get("anyOf")
                            if ref_data:
                                constraints.extend(get_constraints_from_ref(ref_data))
                        else:
                            constraints.append(f"{key}: `{value}`")

            # [MD] Write the basic information for the main property
            name_display = prop_name + (" *" if prop_name in required_props else "")
            markdown_content += f"## {name_display}\n\n"
            markdown_content += f"- **Description**: {prop_details.pop('description', '')}\n"
            if prop_details.get("type"):
                markdown_content += f"- **Type**: `{prop_details.pop('type', '')}`\n"
            if prop_details.get("example"):
                markdown_content += f"- **Example**: `{prop_details.pop('example', '')}`\n"

            for key, value in prop_details.items():
                if key == "enum":
                    constraints.append(f"{key}: {', '.join([f'`{v}`' for v in value])}")
                else:
                    constraints.append(f"{key}: `{value}`")

            # [MD] Write the constraints for the main property
            if constraints:
                markdown_content += f"- **Constraints**: {', '.join(constraints)}\n"

            markdown_content += "\n"

    return markdown_content


def generate_docs(source_dir, output_dir):
    json_files = glob.glob(os.path.join(source_dir, "*", "depositar-dp-profile.json"))
    if not json_files:
        print(f"Warning: No JSON files found in {source_dir}. Skipping.")
        return

    for json_path in json_files:
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                schema = json.load(f)
                Draft7Validator.check_schema(schema)
        except (json.JSONDecodeError, FileNotFoundError) as e:
            print(f"Error processing {json_path}: {e}. Skipping this file.")
            continue
        except SchemaError as e:
            print("Validation failed: Your JSON schema's syntax is not "
                  "compliant with Draft-07. Skipping this file.")
            print(f"Error message: {e.message}")
            print(f"Error path: {list(e.path)}")
            continue

        version = json_path.split(os.sep)[-2]

        # Title (h1)
        markdown_content = f"# {schema['title']} {version}\n\n"

        # Main description
        markdown_content += DESCRIPTION_MD

        # URL for the profile
        markdown_content += (
            "Source: [depositar-dp-profile.json](https://github.com/depositar/"
            f"ckanext-data-depositario/blob/master/depositar-dp/{version}/"
            "depositar-dp-profile.json)\n\n"
        )

        # Content
        markdown_content += get_properties_data(schema)

        version_dir = os.path.basename(os.path.dirname(json_path))
        target_dir = os.path.join(output_dir, version_dir)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        output_path = os.path.join(target_dir, "index.md")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
            print(f"Markdown content generated at {output_path}")


class BuildDPProfileDoc(Command):
    description = "Builds documentation for Data Package profiles."
    user_options = [
        ("source-dir=", None, "Source directory for Data Package profiles."),
        ("output-dir=", None, "Output directory for generated documentation "
                              "(can be a comma-separated list).")
    ]

    def initialize_options(self):
        self.source_dir = "depositar-dp"
        self.output_dir = "doc_en/appendix/datapackage"

    def finalize_options(self):
        self.output_dirs = [d.strip() for d in self.output_dir.split(",")]

    def run(self):
        for i in range(len(self.output_dirs)):
            source_dir = self.source_dir
            output_dir = self.output_dirs[i]
            print(f"Processing from '{source_dir}' to '{output_dir}'...")
            generate_docs(source_dir, output_dir)
