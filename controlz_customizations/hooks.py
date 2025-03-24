app_name = "controlz_customizations"
app_title = "Controlz Customizations"
app_publisher = "Controlz Customizations"
app_description = "Controlz Customizations"
app_email = "controlz@controlz.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/controlz_customizations/css/controlz_customizations.css"
# app_include_js = "/assets/controlz_customizations/js/controlz_customizations.js"

# include js, css files in header of web template
# web_include_css = "/assets/controlz_customizations/css/controlz_customizations.css"
# web_include_js = "/assets/controlz_customizations/js/controlz_customizations.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "controlz_customizations/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Order" : "public/js/sales_order.js"
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "controlz_customizations/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }
after_migrate = "controlz_customizations.custom_field.setup_custom_fields"
# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "controlz_customizations.utils.jinja_methods",
# 	"filters": "controlz_customizations.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "controlz_customizations.install.before_install"
# after_install = "controlz_customizations.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "controlz_customizations.uninstall.before_uninstall"
# after_uninstall = "controlz_customizations.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "controlz_customizations.utils.before_app_install"
# after_app_install = "controlz_customizations.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "controlz_customizations.utils.before_app_uninstall"
# after_app_uninstall = "controlz_customizations.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "controlz_customizations.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Stock Entry": {
		"on_submit": "controlz_customizations.stock_entry.on_submit",
		"on_cancel": "controlz_customizations.stock_entry.on_cancel",
	},
    "Delivery Note": {
        "on_submit": "controlz_customizations.bin.delivery_note_on_submit_cancel",
        "on_cancel": "controlz_customizations.bin.delivery_note_on_submit_cancel",
	},
    "Purchase Receipt": {
        "on_submit": "controlz_customizations.bin.purchase_receipt_on_submit_cancel",
        "on_cancel": "controlz_customizations.bin.purchase_receipt_on_submit_cancel"
	},
    "Sales Order": {
        "on_submit": "controlz_customizations.bin.sales_order_on_submit_cancel",
        "on_cancel": "controlz_customizations.bin.sales_order_on_submit_cancel"
	}
    
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"controlz_customizations.tasks.all"
# 	],
# 	"daily": [
# 		"controlz_customizations.tasks.daily"
# 	],
# 	"hourly": [
# 		"controlz_customizations.tasks.hourly"
# 	],
# 	"weekly": [
# 		"controlz_customizations.tasks.weekly"
# 	],
# 	"monthly": [
# 		"controlz_customizations.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "controlz_customizations.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "controlz_customizations.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "controlz_customizations.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["controlz_customizations.utils.before_request"]
# after_request = ["controlz_customizations.utils.after_request"]

# Job Events
# ----------
# before_job = ["controlz_customizations.utils.before_job"]
# after_job = ["controlz_customizations.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"controlz_customizations.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

