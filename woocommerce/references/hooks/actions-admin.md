# WooCommerce Actions: Admin

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### add_meta_boxes
**Args:** $this->screen_id, $this->order
**Tags:** #action

### add_meta_boxes_$THIS->SCREEN_ID
**Tags:** #action

### admin_enqueue_scripts
**Tags:** #action

### admin_head
**Tags:** #action

### admin_print_styles
**Tags:** #action

### wc_admin_daily
**Tags:** #action

### wc_logs_settings_form_fields
**Params:** bool $enabled
**Since:** 8.6.0 | **Tags:** #action
Action fires after the built-in logging settings controls have been rendered. This is intended as a way to allow other logging settings controls to be added by extensions.

### woocommerce_$THIS->ORDER_TYPE_list_table_custom_column
**Tags:** #action

### woocommerce_admin_after_product_gallery_item
**Args:** $thepostid, $attachment_id
**Tags:** #action

### woocommerce_admin_attribute_types
**Tags:** #action

### woocommerce_admin_css
**Tags:** #action

### woocommerce_admin_field_$VALUE[type]
**Tags:** #action

### woocommerce_admin_field_payment_gateways
1.5.7
**Since:** Fires before the payment gateways settings fields are rendered. | **Tags:** #action

### woocommerce_admin_installed
**Tags:** #action

### woocommerce_admin_key_fields
**Args:** $key_data
**Tags:** #action

### woocommerce_admin_order_actions_end
**Params:** WC_Order $order
**Since:** 6.7.0 | **Tags:** #action
Fires after the order action buttons (within the actions column for the order list table) are rendered.

### woocommerce_admin_order_actions_start
**Params:** WC_Order $order
**Since:** 6.7.0 | **Tags:** #action
Fires before the order action buttons (within the actions column for the order list table) are registered.

### woocommerce_admin_order_data_after_billing_address
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_data_after_order_details
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_data_after_payment_info
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_data_after_shipping_address
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_data_header_right
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_item_headers
**Args:** $order
**Tags:** #action

### woocommerce_admin_order_item_values
**Args:** null, $item, absint( $item_id )
**Tags:** #action

### woocommerce_admin_order_items_after_fees
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_items_after_line_items
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_items_after_refunds
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_items_after_shipping
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_preview_end
**Tags:** #action

### woocommerce_admin_order_preview_start
**Tags:** #action

### woocommerce_admin_order_totals_after_discount
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_totals_after_refunded
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_totals_after_shipping
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_totals_after_tax
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_order_totals_after_total
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_admin_payment_gateway_connection_return
**Args:** $gateway_id
**Tags:** #action

### woocommerce_admin_payments_extension_suggestion_incentive_dismissed
**Params:** string $id, string $suggestion_id, string $context
**Since:** 9.9.0 | **Tags:** #action
Fires when a payments extension suggestion incentive is dismissed.

### woocommerce_admin_process_product_object
**Args:** $product
**Tags:** #action

### woocommerce_admin_process_variation_object
**Params:** object $variation, int $i
**Since:** 3.8.0 | **Tags:** #action
Set variation props before save.

### woocommerce_admin_status_content_$CURRENT_TAB
**Tags:** #action

### woocommerce_admin_user_actions_end
**Args:** $user
**Tags:** #action

### woocommerce_admin_user_actions_start
**Args:** $user
**Tags:** #action

### woocommerce_after_dashboard_status_widget
**Args:** $reports
**Tags:** #action

### woocommerce_attribute_added
**Params:** int $id, array $data
**Tags:** #action
Attribute added.

### woocommerce_attribute_deleted
**Params:** int $id, string $name, string $taxonomy
**Tags:** #action
After deleting an attribute.

### woocommerce_attribute_updated
**Params:** int $id, array $data, string $old_slug
**Tags:** #action
Attribute updated.

### woocommerce_page_created
**Args:** $page_id, $page_data
**Tags:** #action

### woocommerce_page_wc-addons_connection_error
**Args:** $raw_promotions->get_error_message()
**Tags:** #action

### woocommerce_page_wc_addons_connection_error
**Params:** string $error_message
**Since:** 6.1.0 | **Tags:** #action
Hook fired when there is a connection error with WooCommerce.com.

### woocommerce_register_post_type
**Tags:** #action

### woocommerce_settings_$CURRENT_TAB
**Tags:** #action

### woocommerce_settings_page_init
**Tags:** #action

### woocommerce_settings_sanitize_title$VALUE[id]
**Tags:** #action

### woocommerce_settings_sanitize_title$VALUE[id]_after
**Tags:** #action

### woocommerce_settings_sanitize_title$VALUE[id]_end
**Tags:** #action

### woocommerce_settings_save_$CURRENT_TAB
**Tags:** #action

### woocommerce_settings_saved
**Tags:** #action

### woocommerce_settings_start
**Tags:** #action

### woocommerce_settings_tabs
**Tags:** #action

### woocommerce_settings_tabs_$CURRENT_TAB
**Tags:** #action

### woocommerce_settings_updated
**Params:** array $updated_settings, string $rest_base
**Since:** 4.0.0 | **Tags:** #action
Fires when WooCommerce settings are updated.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
