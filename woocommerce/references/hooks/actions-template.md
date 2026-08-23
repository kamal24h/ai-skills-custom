# WooCommerce Actions: Template

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_account_downloads
**Args:** $has_downloads
**Tags:** #action

### woocommerce_after_account_navigation
**Tags:** #action

### woocommerce_after_account_orders
**Args:** $has_orders
**Tags:** #action

### woocommerce_after_available_downloads
**Tags:** #action

### woocommerce_after_edit_address_form_$LOAD_ADDRESS
**Tags:** #action

### woocommerce_after_lost_password_confirmation_message
**Tags:** #action

### woocommerce_after_lost_password_form
**Tags:** #action

### woocommerce_after_main_content
**Tags:** #action

### woocommerce_after_mini_cart
**Tags:** #action

### woocommerce_after_order_details
**Params:** WC_Order $order
**Since:** 4.4.0 | **Tags:** #action
Action hook fired after the order details.

### woocommerce_after_quantity_input_field
**Tags:** #action

### woocommerce_after_reset_password_form
**Tags:** #action

### woocommerce_after_shop_loop
**Tags:** #action

### woocommerce_after_shop_loop_item
**Tags:** #action

### woocommerce_after_shop_loop_item_title
**Tags:** #action

### woocommerce_after_single_variation
**Tags:** #action

### woocommerce_after_subcategory
**Args:** $category
**Tags:** #action

### woocommerce_after_subcategory_title
**Args:** $category
**Tags:** #action

### woocommerce_after_variations_form
**Tags:** #action

### woocommerce_after_variations_table
**Tags:** #action

### woocommerce_before_account_downloads
**Args:** $has_downloads
**Tags:** #action

### woocommerce_before_account_navigation
**Tags:** #action

### woocommerce_before_account_orders
**Args:** $has_orders
**Tags:** #action

### woocommerce_before_account_orders_pagination
**Tags:** #action

### woocommerce_before_available_downloads
**Tags:** #action

### woocommerce_before_edit_address_form_$LOAD_ADDRESS
**Tags:** #action

### woocommerce_before_lost_password_confirmation_message
**Tags:** #action

### woocommerce_before_lost_password_form
**Tags:** #action

### woocommerce_before_main_content
**Tags:** #action

### woocommerce_before_mini_cart
**Tags:** #action

### woocommerce_before_quantity_input_field
**Tags:** #action

### woocommerce_before_reset_password_form
**Tags:** #action

### woocommerce_before_shop_loop
**Tags:** #action

### woocommerce_before_shop_loop_item
**Tags:** #action

### woocommerce_before_shop_loop_item_title
**Tags:** #action

### woocommerce_before_single_variation
**Tags:** #action

### woocommerce_before_subcategory
**Args:** $category
**Tags:** #action

### woocommerce_before_subcategory_title
**Args:** $category
**Tags:** #action

### woocommerce_before_thankyou
**Args:** $order->get_id()
**Tags:** #action

### woocommerce_before_variations_form
**Tags:** #action

### woocommerce_no_products_found
**Tags:** #action

### woocommerce_shop_loop
**Tags:** #action

### woocommerce_shop_loop_header
**Tags:** #action

### woocommerce_shop_loop_item_title
**Tags:** #action

### woocommerce_shop_loop_subcategory_title
**Args:** $category
**Tags:** #action

### woocommerce_sidebar
**Tags:** #action

### woocommerce_widget_price_filter_end
**Args:** $args
**Tags:** #action

### woocommerce_widget_price_filter_start
**Args:** $args
**Tags:** #action

### woocommerce_breadcrumb
**Args:** $breadcrumbs, $args
**Tags:** #action

### woocommerce_shortcode_$THIS->TYPE_loop_no_results
**Tags:** #action

### woocommerce_shortcode_after_$THIS->TYPE_loop
**Tags:** #action

### woocommerce_shortcode_before_$THIS->TYPE_loop
**Tags:** #action

### woocommerce_widget_layered_nav_filters_end
**Params:** array $args, array $instance
**Since:** 7.6.0 | **Tags:** #action
Allow 3rd party developers to add their own filters to end the Layered Navigation Filters Widget.

### woocommerce_widget_layered_nav_filters_start
**Params:** array $args, array $instance
**Since:** 7.6.0 | **Tags:** #action
Allow 3rd party developers to add their own filters to start the Layered Navigation Filters Widget.

### woocommerce_before_delete_$POST_TYPE
**Tags:** #action

### woocommerce_before_delete_order
**Params:** int $order_id, WC_Order $order
**Since:** 8.0.0 | **Tags:** #action
Fires immediately before an order is deleted from the database.

### woocommerce_before_trash_order
**Params:** int $order_id, WC_Order $order
**Since:** 8.0.0 | **Tags:** #action
Fires immediately before an order is trashed.

### woocommerce_after_$THIS->OBJECT_TYPE_object_save
**Tags:** #action

### woocommerce_after_add_attribute_fields
**Tags:** #action

### woocommerce_after_calculate_totals
**Args:** $this
**Tags:** #action

### woocommerce_after_edit_attribute_fields
**Tags:** #action

### woocommerce_after_get_rates_for_package
**Params:** array $package, WC_Shipping_Method $shipping_method
**Since:** 4.3.0 | **Tags:** #action
Fires after getting shipping rates for a package.

### woocommerce_after_pay_action
**Args:** $order
**Tags:** #action

### woocommerce_after_register_post_type
**Tags:** #action

### woocommerce_after_register_taxonomy
**Tags:** #action

### woocommerce_after_save_address_validation
**Params:** int $user_id, string $address_type, array $address, WC_Customer $customer
**Since:** 3.6.0 | **Tags:** #action
Hook: woocommerce_after_save_address_validation. Allow developers to add custom validation logic and throw an error to prevent save.

### woocommerce_after_set_term_order
**Args:** $term, $index, $taxonomy
**Tags:** #action

### woocommerce_after_settings_$CURRENT_TAB
**Tags:** #action

### woocommerce_after_template_part
**Args:** $action_args['template_name'], $action_args['template_path'], $action_args['located'], $action_args['args']
**Tags:** #action

### woocommerce_before_$THIS->OBJECT_TYPE_object_save
**Tags:** #action

### woocommerce_before_add_attribute_fields
**Tags:** #action

### woocommerce_before_attribute_delete
**Params:** int $id, string $name, string $taxonomy
**Tags:** #action
Before deleting an attribute.

### woocommerce_before_edit_attribute_fields
**Tags:** #action

### woocommerce_before_get_rates_for_package
**Params:** array $package, WC_Shipping_Method $shipping_method
**Since:** 4.3.0 | **Tags:** #action
Fires before getting shipping rates for a package.

### woocommerce_before_pay_action
**Args:** $order
**Tags:** #action

### woocommerce_before_settings_$CURRENT_TAB
**Tags:** #action

### woocommerce_before_template_part
**Args:** $action_args['template_name'], $action_args['template_path'], $action_args['located'], $action_args['args']
**Tags:** #action

### woocommerce_block_template_after_add_block
**Tags:** #action

### woocommerce_block_template_after_add_block_error
**Tags:** #action

### woocommerce_block_template_after_add_hide_condition
**Tags:** #action

### woocommerce_block_template_after_remove_block
**Tags:** #action

### woocommerce_block_template_after_remove_block_error
**Tags:** #action

### woocommerce_block_template_after_remove_hide_condition
**Tags:** #action

### woocommerce_block_template_area_$THIS->GET_ROOT_TEMPLATE->GET_AREA_after_add_block_$BLOCK->GET_ID
**Tags:** #action

### woocommerce_block_template_area_$THIS->GET_ROOT_TEMPLATE->GET_AREA_after_remove_block_$BLOCK->GET_ID
**Tags:** #action

### woocommerce_layout_template_after_instantiation
**Tags:** #action

### woocommerce_widget_field_$SETTING[type]
**Tags:** #action

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
