===================
How to provide data
===================

You can not directly register on |site_name| currently. If you or your organization
want to upload data to |site_name|, please create an organization first through the
following steps:

.. hint::

   We provide a demo system at https://demo.depositar.io with the same features
   as |site_name| for evaluation purposes. You can create an account and try
   any functions provided by |site_name|. Please note that all data in this instance
   will be deleted occasionally.

.. note::

   For ease of management, it is suggested to create a new CKAN ``organizaion`` for each person or
   organization to upload datasets.

------------------------
Creating an organization
------------------------

According to whether you have an account on |site_name|, please select one of the following
two methods to create a new organization:

If you don't have an account
=============================

Please send an email with the subject line titled "|site_name|: Apply for an Organization"
to data.contact AT depositar.io providing the following information:

* *E-mail address* -- this will not be visible to other users

* *Organization name*

* *Organization url* -- choose an url using only letters, numbers, - and _ characters.
  The created organization will be located at
  \https://data.depositar.io/organization/[Organization url]

You will receive your results as shown below within 72 hours. And, you are the administrator
of the new organization.

.. image:: /images/invite_user_email.png

Please follow the instructions in the email and reset your password immediately.

If you already have an account
==============================

Please refer to :ref:`creating_an_organization` to create a new organization.

.. note::

   You can learn how to fill in the information above by referring to
   `existing organizations <https://data.depositar.io/organization>`_.

-------------------
Uploading a dataset
-------------------

Then you can go to \https://data.depositar.io/organization/[Organization url],
select the "Add Dataset" button above the search box, and create a dataset.

.. note::

   For adding a new dataset, please refer to :ref:`adding_a_new_dataset`.

-------------------------------
Inviting others to organization
-------------------------------

If you want to invite others to collaborate on datasets, you can invite them to your organization.
From the organization’s page you should see an “Admin” button above the search box.
When you select this, CKAN displays the organization admin page.

Select the "Members" tab, and you will see the organization members page.
Then select the "Add Member" button.

.. image:: /images/invite_user.png

You can invite an user to your organization by his/her email or username in the "Existing User" section.
Note that he/she must have an account.

.. note::

   Due to the CKAN's privilege design, if the person you would like to invite does not have an account,
   please send an email with his/her email address to data.contact AT depositar.io. Then CKAN will send
   an invitation email to his/her.

.. note::

   For access privileges and members management, please refer to :ref:`managing_an_organization`.
