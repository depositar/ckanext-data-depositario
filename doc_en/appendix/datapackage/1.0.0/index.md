# The depositar Data Package 1.0.0

Metadata in the depositar Data Package are expressed in a `datapackage.json` file. It follows the [Data Package](https://datapackage.org/standard/data-package/) specifications and includes generic **Data Package properties** and specific **depositar DP properties**. Properties indicated with `*` are required (i.e. cannot be empty).

Source: [depositar-dp-profile.json](https://github.com/depositar/ckanext-data-depositario/blob/master/depositar-dp/1.0.0/depositar-dp-profile.json)

## resources *

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#resources).
- **Type**: `array`

| Name         | Description                                                                                              | Type     | Example   | Constraints           |
|--------------|----------------------------------------------------------------------------------------------------------|----------|-----------|-----------------------|
| name *       | See [Data Package specification](https://datapackage.org/standard/data-resource/#name).                  |          |           |                       |
| path *       | See [Data Package specification](https://datapackage.org/standard/data-resource/#path-or-data).          |          |           |                       |
| title        | See [Data Package specification](https://datapackage.org/standard/data-resource/#title).                 |          |           |                       |
| description  | See [Data Package specification](https://datapackage.org/standard/data-resource/#description).           |          |           |                       |
| format       | See [Data Package specification](https://datapackage.org/standard/data-resource/#format).                |          |           |                       |
| mediatype    | See [Data Package specification](https://datapackage.org/standard/data-resource/#mediatype).             |          |           |                       |
| encoding     | See [Data Package specification](https://datapackage.org/standard/data-resource/#encoding).              |          |           |                       |
| bytes        | See [Data Package specification](https://datapackage.org/standard/data-resource/#bytes).                 |          |           |                       |
| ckan:id      | The UUID of the resource.                                                                                | `string` |           |                       |
| resource_crs | The coordinate systems of the resource. The EPSG (European Petroleum Survey Group) system has been used. | `number` | 4326      | exclusiveMinimum: `0` |

## name *

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#name). The depositar DP makes this a required property.

## licenses *

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#licenses). The depositar DP makes this a required property and restricts name values.

| Name   | Description   | Type   | Example   | Constraints                                                                                                     |
|--------|---------------|--------|-----------|-----------------------------------------------------------------------------------------------------------------|
| name   |               |        |           | enum: `notspecified`, `pd`, `cc-zero`, `cc-by`, `cc-by-sa`, `cc-by-nc-sa`, `odc-odbl`, `gfdl`, `twogd`, `other` |

## title

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#title).

## description

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#description).

## created

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#created).

## keywords

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#keywords).

## contributors *

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#contributors). The depositar DP makes this a required property and restricts role values. Can include people and organizations.

| Name   | Description   | Type   | Example   | Constraints                  |
|--------|---------------|--------|-----------|------------------------------|
| roles  |               |        |           | enum: `author`, `maintainer` |

## sources

- **Description**: See [Data Package specification](https://datapackage.org/standard/data-package/#sources).

## ckan:id

- **Description**: The UUID of the dataset.
- **Type**: `string`

## data_type *

- **Description**: The type of the dataset. The [PARSE.Insight Content-types](http://gfzpublic.gfz-potsdam.de/pubman/item/escidoc:1397899:6/component/escidoc:1398549/re3data_schema_documentation_v3_0.pdf) has been used.
- **Type**: `array`
- **Constraints**: enum: `archive`, `code`, `config`, `database`, `doc`, `graphic`, `image`, `multimedia`, `network`, `raw`, `science`, `software`, `structured`, `text`, `other`, uniqueItems: `True`, minItems: `1`

## wd_keywords

- **Description**: The Wikidata items for keywords to describe the dataset.
- **Type**: `array`
- **Constraints**: uniqueItems: `True`

## language

- **Description**: The language of the dataset. Must be a language defined in ISO 639-3.
- **Type**: `array`
- **Constraints**: uniqueItems: `True`

## remarks

- **Description**: Some supplementary information for the dataset. Markdown is encouraged.
- **Type**: `string`
- **Constraints**: format: `textarea`

## temp_res

- **Description**: The precision of a measurement with respect to time. It can be the minimal time interval between subsequent examinations, or the maximum time error when the time period is uncertain.
- **Type**: `string`
- **Constraints**: enum: `yearly`, `daily`, `monthly`

## start_time

- **Description**: The time related to contents of the dataset, not the time when the resources in the dataset were created or finished.
- **Constraints**: patterns: `^[0-9]{4}$`, `^([0-9]{4})-(1[0-2]|0[1-9])$`, `^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$`

## end_time

- **Description**: The time related to contents of the dataset, not the time when the resources in the dataset were created or finished.
- **Constraints**: patterns: `^[0-9]{4}$`, `^([0-9]{4})-(1[0-2]|0[1-9])$`, `^([0-9]{4})-(1[0-2]|0[1-9])-(3[01]|[12][0-9]|0[1-9])$`

## spatial

- **Description**: A GeoJSON text to describe the spatial coverage of the dataset.
- **Type**: `object`

## x_min

- **Description**: Westmost longitude of the spatial extent.
- **Type**: `number`
- **Constraints**: minimum: `-180`, maximum: `180`

## x_max

- **Description**: Eastmost longitude of the spatial extent.
- **Type**: `number`
- **Constraints**: minimum: `-180`, maximum: `180`

## y_min

- **Description**: Southmost latitude of the spatial extent.
- **Type**: `number`
- **Constraints**: minimum: `-90`, maximum: `90`

## y_max

- **Description**: Northmost latitude of the spatial extent.
- **Type**: `number`
- **Constraints**: minimum: `-90`, maximum: `90`

## spatial_res

- **Description**: Spatial resolution (in meter) of the dataset.
- **Type**: `number`
- **Constraints**: exclusiveMinimum: `0`

## created_time

- **Description**: The time when the resources in the dataset were created.
- **Type**: `string`
- **Constraints**: pattern: `^\d{4}(-\d{2})?(-\d{2})?$`

## process_step

- **Description**: Steps of data generating process. Markdown is encouraged.
- **Type**: `string`
- **Constraints**: format: `textarea`

## contact_person

- **Description**: The person responsible for maintaining the dataset.
- **Type**: `string`

## contact_email

- **Description**: The email of the person responsible for maintaining the dataset.
- **Type**: `string`
- **Constraints**: format: `email`

