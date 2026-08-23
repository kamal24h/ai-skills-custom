# WooCommerce Filters: Email

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_email_body_display_section_divider
**Params:** bool $display_section_divider
**Since:** 10.6.0 | **Tags:** #filter
Filter whether to display the section divider in the email body.

### woocommerce_email_footer_text
**Params:** string $email_footer_text
**Since:** 4.0.0 | **Tags:** #filter
Provides control over the email footer text used for most order emails.

### woocommerce_email_header_image_url
**Params:** string $url
**Since:** 10.7.0 | **Tags:** #filter
Filter the URL used for the email header image/logo link. Return an empty string to disable the link.

### woocommerce_email_intro_content
**Args:** $intro_content, $notification
**Tags:** #filter

### woocommerce_email_order_item_quantity
**Params:** string $qty_display, WC_Order_Item_Product $item
**Since:** 2.4.0 | **Tags:** #filter
Email Order Item Quantity hook.

### woocommerce_emails_general_block_content_emails_without_order_details
**Params:** array $emails_without_order_details
**Since:** 10.5.0 | **Tags:** #filter
Filter the list of email IDs that should not display order details.

### woocommerce_is_email_preview
**Params:** bool $is_email_preview
**Since:** 9.6.0 | **Tags:** #filter
This filter is documented in templates/emails/email-styles.php

### woocommerce_email_fulfillment_items_args
**Params:** array $args
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify the arguments for the email fulfillment items.

### woocommerce_email_order_items_args
**Args:** array(
					'order'               => $order,
					'items'               => $order->get_items(),
					'show_download_links' => $order->is_download_permitted() && ! $args['sent_to_admin'],
					'show_sku'            => $args['show_sku'],
					'show_purchase_note'  => $order->is_paid() && ! $args['sent_to_admin'],
					'show_image'          => $args['show_image'],
					'image_size'          => $args['image_size'],
					'plain_text'          => $args['plain_text'],
					'sent_to_admin'       => $args['sent_to_admin'],
				)
**Tags:** #filter

### woocommerce_email_order_items_table
**Args:** ob_get_clean(), $order
**Tags:** #filter

### woocommerce_get_email_fulfillment_items_table
**Params:** string $html, WC_Order $order, Fulfillment $fulfillment
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify the email fulfillment items table HTML.

### woocommerce_get_username_from_email
**Args:** true
**Tags:** #filter

### wc_payment_gateway_enabled_notification_email_addresses
**Params:** array $email_addresses, WC_Payment_Gateway $gateway
**Since:** 8.5.0 | **Tags:** #filter
Allows adding to the addresses that receive payment gateway enabled notifications.

### woocommerce_allow_restoring_email_locale
**Params:** bool $default_value, WC_Email $email
**Since:** 6.8.0 | **Tags:** #filter
Filter the ability to restore email locale.

### woocommerce_allow_send_queued_transactional_email
**Params:** bool $allow, string $filter, array $args
**Since:** 3.0.0 | **Tags:** #filter
Filter whether to allow sending queued transactional emails.

### woocommerce_allow_switching_email_locale
**Params:** bool $default_value, WC_Email $email
**Since:** 6.8.0 | **Tags:** #filter
Filter the ability to switch email locale.

### woocommerce_bacs_email_instructions_order_status
**Params:** string $terms, object $order
**Since:** 7.4 | **Tags:** #filter
Filter the email instructions order status.

### woocommerce_cheque_email_instructions_order_status
**Params:** string $status, object $order
**Since:** 7.4 | **Tags:** #filter
Filter the email instructions order status.

### woocommerce_defer_transactional_emails
**Params:** bool $defer
**Since:** 3.0.0 | **Tags:** #filter
Filter whether to defer transactional emails.

### woocommerce_email_actions
**Params:** array $email_actions
**Since:** 3.0.0 | **Tags:** #filter
Filter the actions that trigger transactional emails.

### woocommerce_email_additional_content_$THIS->ID
**Tags:** #filter

### woocommerce_email_attachments
**Params:** array $attachments, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the attachments of the low stock notification email.

### woocommerce_email_bcc_recipient_$THIS->ID
**Tags:** #filter

### woocommerce_email_block_template_html
**Params:** string $template_html, \WC_Email $email
**Since:** 10.7.0 | **Tags:** #filter
Filter the email template HTML.

### woocommerce_email_cc_recipient_$THIS->ID
**Tags:** #filter

### woocommerce_email_classes
**Params:** array $emails
**Since:** 3.0.0 | **Tags:** #filter
Filter the email classes.

### woocommerce_email_content_backorder
**Params:** string $message, array $args, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the content of the backorder notification email.

### woocommerce_email_content_low_stock
**Params:** string $message, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the content of the low stock notification email.

### woocommerce_email_content_no_stock
**Params:** string $message, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the content of the no stock notification email.

### woocommerce_email_content_post_data
**Params:** array $post_data, string $email_type, \WC_Email $email
**Since:** 10.5.0 | **Tags:** #filter
Filter the email content post data before creating the post. Allows third-party integrators to modify the post data (title, content, meta, etc.) before the email content post is created.

### woocommerce_email_content_type
**Args:** $content_type, $this, $default_content_type
**Tags:** #filter

### woocommerce_email_customer_details_fields
**Params:** array $fields, bool $sent_to_admin, WC_Order $order
**Since:** 3.2.0 | **Tags:** #filter
Filter the customer details fields.

### woocommerce_email_description
**Args:** $this->description, $this
**Tags:** #filter

### woocommerce_email_downloads_columns
**Params:** array $columns, WC_Order $order
**Since:** 3.2.0 | **Tags:** #filter
Filter the columns of the order downloads table.

### woocommerce_email_editor_integration_personalizer_context_data
**Params:** array $context, \WC_Email $email
**Since:** 10.5.0 | **Tags:** #filter
Filters the context data for email personalization. This filter fires after core defaults are set, allowing extensions to override values like wp_user for custom email types (e.g., WooCommerce Bookings).

### woocommerce_email_editor_logging_threshold
**Params:** string $threshold
**Since:** 10.2.0 | **Tags:** #filter
Controls the logging threshold for the email editor.

### woocommerce_email_enabled_$THIS->ID
**Tags:** #filter

### woocommerce_email_format_string
**Args:** str_replace( $find, $replace, $string ), $this
**Tags:** #filter

### woocommerce_email_format_string_find
**Args:** $legacy_find, $this
**Tags:** #filter

### woocommerce_email_format_string_replace
**Args:** $legacy_replace, $this
**Tags:** #filter

### woocommerce_email_from_address
**Args:** get_option( 'woocommerce_email_from_address' ), $this, $from_email
**Tags:** #filter

### woocommerce_email_from_name
**Params:** string|mixed $from_name, WC_Email $email, string $default_from_name
**Since:** 2.1.0 | **Tags:** #filter
Filters the "from" name for outgoing emails.

### woocommerce_email_get_option
**Args:** $value, $this, $value, $key, $empty_value
**Tags:** #filter

### woocommerce_email_group_title
**Params:** string $title, string $email_group, array $email_groups
**Since:** 10.3.0 | **Tags:** #filter
Filter the email group title.

### woocommerce_email_groups
**Params:** array $email_groups
**Since:** 10.3.0 | **Tags:** #filter
Filter the available email groups.

### woocommerce_email_headers
**Params:** string $headers, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the headers of the low stock notification email.

### woocommerce_email_heading_$THIS->ID
**Tags:** #filter

### woocommerce_email_heading_customer_invoice
**Args:** $this->format_string( $heading ), $this->object, $this
**Tags:** #filter

### woocommerce_email_heading_customer_invoice_paid
**Args:** $this->format_string( $heading ), $this->object, $this
**Tags:** #filter

### woocommerce_email_heading_customer_refunded_order
**Params:** string $heading, WC_Order $order, WC_Email_Customer_POS_Refunded_Order $email
**Since:** 3.7.0 | **Tags:** #filter
Filter the email heading for customer refunded order.

### woocommerce_email_order_meta_fields
**Params:** array $fields, bool $sent_to_admin, WC_Order $order
**Since:** 3.0.0 | **Tags:** #filter
Filter the order meta fields.

### woocommerce_email_order_meta_keys
**Params:** array $fields, bool $sent_to_admin
**Since:** 2.3.0 | **Tags:** #filter
Deprecated woocommerce_email_order_meta_keys filter.

### woocommerce_email_preheader$THIS->ID
**Tags:** #filter

### woocommerce_email_preview_dummy_address
**Params:** array $address, string $email_type
**Since:** 9.6.0 | **Tags:** #filter
A dummy address used in email preview as billing and shipping one.

### woocommerce_email_preview_dummy_downloadable_product
**Params:** WC_Product $product, string $email_type
**Since:** 10.3.0 | **Tags:** #filter
A dummy downloadable WC_Product used in email preview.

### woocommerce_email_preview_dummy_order
**Params:** WC_Order $order, string $email_type
**Since:** 9.6.0 | **Tags:** #filter
A dummy WC_Order used in email preview.

### woocommerce_email_preview_dummy_product
**Params:** WC_Product $product, string $email_type
**Since:** 9.6.0 | **Tags:** #filter
A dummy WC_Product used in email preview.

### woocommerce_email_preview_dummy_product_variation
**Params:** WC_Product_Variation $variation, string $email_type
**Since:** 9.7.0 | **Tags:** #filter
A dummy WC_Product_Variation used in email preview.

### woocommerce_email_preview_email_content_setting_ids
**Params:** array $setting_ids, string $email_id
**Since:** 9.8.0 | **Tags:** #filter
Filter the email content setting IDs for specific email. Email preview automatically refreshes when these settings are changed.

### woocommerce_email_preview_email_style_setting_ids
**Params:** array $setting_ids
**Since:** 9.8.0 | **Tags:** #filter
Filter the email style setting IDs. Email preview automatically refreshes when these settings are changed.

### woocommerce_email_preview_placeholders
**Params:** array $placeholders, string $email_type, mixed $email_object
**Since:** 9.9.0 | **Tags:** #filter
Placeholders for email preview.

### woocommerce_email_recipient_$THIS->ID
**Tags:** #filter

### woocommerce_email_recipient_backorder
**Params:** string $recipient, array $args, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the recipient of the backorder notification email.

### woocommerce_email_recipient_low_stock
**Params:** string $recipient, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the recipient of the low stock notification email.

### woocommerce_email_recipient_no_stock
**Params:** string $recipient, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the recipient of the no stock notification email.

### woocommerce_email_reply_to_address
**Params:** string $reply_to_email, WC_Email $email, string $default_email
**Since:** 10.4.0 | **Tags:** #filter
Filter the reply-to address for emails.

### woocommerce_email_reply_to_enabled
**Params:** bool $enabled, WC_Email $email
**Since:** 10.4.0 | **Tags:** #filter
Filter whether reply-to is enabled for emails.

### woocommerce_email_reply_to_name
**Params:** string $reply_to_name, WC_Email $email, string $default_name
**Since:** 10.4.0 | **Tags:** #filter
Filter the reply-to name for emails.

### woocommerce_email_restore_locale
**Args:** true
**Tags:** #filter

### woocommerce_email_setting_columns
**Params:** array $columns
**Since:** 2.1.0 | **Tags:** #filter
Filters the columns displayed in the email settings table.

### woocommerce_email_settings
**Params:** array $settings
**Since:** 2.1.0 | **Tags:** #filter
Filters the email settings array.

### woocommerce_email_setup_locale
**Args:** true
**Tags:** #filter

### woocommerce_email_stock_notification_base_text_color
**Args:** wc_light_or_dark( $base, '#202020', '#ffffff' ), $email
**Tags:** #filter

### woocommerce_email_stock_notification_button_link
**Params:** string $button_href, Notification $notification, WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter the button href.

### woocommerce_email_stock_notification_button_text
**Params:** string $button_text, Notification $notification, WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter the button text.

### woocommerce_email_stock_notification_emails_to_style
**Args:** self::$email_ids
**Tags:** #filter

### woocommerce_email_stock_notification_intro_content
**Args:** $this->format_string( $this->get_option_or_transient( 'intro_content', $this->get_default_intro_content() ) ), $this->object, $this
**Tags:** #filter

### woocommerce_email_stock_notification_verify_button_text
**Params:** string $button_text, Notification $notification, WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter the button text.

### woocommerce_email_styles
**Params:** string $css, \WC_Email $email
**Since:** 2.3.0 | **Tags:** #filter
Provides an opportunity to filter the CSS styles included in e-mails.

### woocommerce_email_subject_$THIS->ID
**Tags:** #filter

### woocommerce_email_subject_backorder
**Params:** string $subject, array $args, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the subject of the backorder notification email.

### woocommerce_email_subject_customer_invoice
**Args:** $this->format_string( $subject ), $this->object, $this
**Tags:** #filter

### woocommerce_email_subject_customer_invoice_paid
**Args:** $this->format_string( $subject ), $this->object, $this
**Tags:** #filter

### woocommerce_email_subject_customer_refunded_order
**Params:** string $subject, object|bool $order, WC_Email_Customer_Refunded_Order $email
**Since:** 3.7.0 | **Tags:** #filter
Filter the email subject for customer refunded order.

### woocommerce_email_subject_low_stock
**Params:** string $subject, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the subject of the low stock notification email.

### woocommerce_email_subject_no_stock
**Params:** string $subject, WC_Product $product, null $null
**Since:** 3.0.0 | **Tags:** #filter
Filter the subject of the no stock notification email.

### woocommerce_email_title
**Args:** $this->title, $this
**Tags:** #filter

### woocommerce_emails_api_settings_schema_validate_and_sanitize_settings
**Params:** array $values_to_update, array $settings_by_id
**Since:** 10.6.0 | **Tags:** #filter
Filters the values to update before validation and sanitization.

### woocommerce_emails_settings_schema_validate_and_sanitize_settings
**Params:** array $validated, WC_Email $email, array $values
**Since:** 10.6.0 | **Tags:** #filter
Filters the validated settings after validation and sanitization.

### woocommerce_mail_callback
**Args:** 'wp_mail', $this
**Tags:** #filter

### woocommerce_mail_callback_params
**Args:** array( $to, wp_specialchars_decode( $subject ), $message, $headers, $attachments ), $this
**Tags:** #filter

### woocommerce_mail_content
**Args:** $this->style_inline( $message )
**Tags:** #filter

### woocommerce_mail_style_inline_callback
**Params:** callable $style_inline_callback, string|null $content, WC_Email $email
**Since:** 10.2.0 | **Tags:** #filter
Filter to allow the ability to override the email inline styling method.

### woocommerce_prepare_email_for_preview
**Params:** WC_Email $email
**Since:** 9.6.0 | **Tags:** #filter
Allow to modify the email object before rendering the preview to add additional data.

### woocommerce_registration_error_email_exists
**Params:** string $message, string $email
**Since:** 3.3.0 | **Tags:** #filter
Filter the notice shown when a customer tries to register with an existing email address.

### woocommerce_report_export_email_labels
**Params:** string[] $labels
**Since:** 9.9.0 | **Tags:** #filter
Used to customise report email labels.

### woocommerce_tracker_admin_email
**Args:** get_option( 'admin_email' )
**Tags:** #filter

### woocommerce_transactional_emails_for_block_editor
**Params:** array $transactional_emails
**Since:** 9.9.0 | **Tags:** #filter
Filter the transactional emails for the block editor.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
