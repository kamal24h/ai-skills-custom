# WooCommerce Actions: Email

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_email_after_fulfillment_table
**Params:** WC_Order $order, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 2.5.0 | **Tags:** #action
Action hook to add custom content after fulfillment details in email.

### woocommerce_email_after_order_table
**Params:** WC_Order $order, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 2.5.0 | **Tags:** #action
Action hook to add custom content after order details in email.

### woocommerce_email_before_fulfillment_table
**Params:** WC_Order $order, Fulfillment $fulfillment, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 2.5.0 | **Tags:** #action
Action hook to add custom content before fulfillment details in email.

### woocommerce_email_before_order_table
**Params:** WC_Order $order, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 2.5.0 | **Tags:** #action
Action hook to add custom content before order details in email.

### woocommerce_email_customer_address_section
**Params:** string $type, WC_Order $order, bool $sent_to_admin, bool $plain_text
**Since:** 8.6.0 | **Tags:** #action
Fires after the core address fields in emails.

### woocommerce_email_customer_details
**Params:** WC_Order $order, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 2.5.0 | **Tags:** #action
Hook for woocommerce_email_customer_details.

### woocommerce_email_downloads_column_$COLUMN_ID
**Tags:** #action

### woocommerce_email_footer
**Params:** null $null
**Since:** 3.0.0 | **Tags:** #action
Action hook for email footer.

### woocommerce_email_fulfillment_details
**Params:** WC_Order $order, Fulfillment $fulfillment, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 10.1.0 | **Tags:** #action
Hook for the woocommerce_email_fulfillment_details.

### woocommerce_email_fulfillment_meta
**Params:** WC_Order $order, Fulfillment $fulfillment, bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 10.1.0 | **Tags:** #action
Hook for the woocommerce_email_fulfillment_meta.

### woocommerce_email_general_block_content
**Params:** bool $sent_to_admin, bool $plain_text, WC_Email $email
**Since:** 10.5.0 | **Tags:** #action
Action hook for email classes to hook into the general block email template.

### woocommerce_email_header
**Params:** string $email_heading, null $null
**Since:** 3.0.0 | **Tags:** #action
Action hook for email header.

### woocommerce_email_order_details
**Args:** $order, $sent_to_admin, $plain_text, $email
**Tags:** #action

### woocommerce_email_order_meta
**Args:** $order, $sent_to_admin, $plain_text, $email
**Tags:** #action

### woocommerce_email_stock_notification_product
**Args:** $product, $notification, $plain_text, $email
**Tags:** #action

### woocommerce_pos_email_footer
**Args:** $email
**Tags:** #action

### woocommerce_pos_email_header
**Args:** $email_heading, $email
**Tags:** #action

### woocommerce_copy_email_template
**Params:** string $template_type, string $email
**Tags:** #action
Action hook fired after copying email template file.

### woocommerce_delete_email_template
**Params:** string $template, string $email
**Tags:** #action
Action hook fired after deleting template file.

### woocommerce_email
**Params:** WC_Emails $this
**Since:** 3.0.0 | **Tags:** #action
Action hook for email classes to hook into.

### woocommerce_email_sent
**Params:** bool $return, string $id, WC_Email $email
**Since:** 5.6.0 | **Tags:** #action
Action hook fired when an email is sent.

### woocommerce_email_setting_column_$KEY
**Tags:** #action

### woocommerce_email_settings_after
**Params:** string $email
**Tags:** #action
Action hook fired after displaying email settings.

### woocommerce_email_settings_before
**Params:** string $email
**Tags:** #action
Action hook fired before displaying email settings.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
