# WooCommerce Actions: Product

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_add_to_cart_button
**Tags:** #action

### woocommerce_after_add_to_cart_form
**Tags:** #action

### woocommerce_after_add_to_cart_quantity
**Tags:** #action

### woocommerce_after_single_product
**Tags:** #action

### woocommerce_after_single_product_summary
**Tags:** #action

### woocommerce_before_add_to_cart_button
**Tags:** #action

### woocommerce_before_add_to_cart_form
**Tags:** #action

### woocommerce_before_add_to_cart_quantity
**Tags:** #action

### woocommerce_before_single_product
**Tags:** #action

### woocommerce_before_single_product_summary
**Tags:** #action

### woocommerce_grouped_product_list_after
**Args:** $grouped_product_columns, $quantites_required, $product
**Tags:** #action

### woocommerce_grouped_product_list_after_$COLUMN_ID
**Tags:** #action

### woocommerce_grouped_product_list_before
**Args:** $grouped_product_columns, $quantites_required, $product
**Tags:** #action

### woocommerce_grouped_product_list_before_$COLUMN_ID
**Tags:** #action

### woocommerce_product_additional_information
**Args:** $product
**Tags:** #action

### woocommerce_product_after_tabs
**Tags:** #action

### woocommerce_product_meta_end
**Tags:** #action

### woocommerce_product_meta_start
**Tags:** #action

### woocommerce_product_thumbnails
**Tags:** #action

### woocommerce_single_product_summary
**Tags:** #action

### woocommerce_single_variation
**Tags:** #action

### woocommerce_widget_product_item_end
**Args:** $args
**Tags:** #action

### woocommerce_widget_product_item_start
**Args:** $args
**Tags:** #action

### woocommerce_widget_product_review_item_end
**Args:** $args
**Tags:** #action

### woocommerce_widget_product_review_item_start
**Args:** $args
**Tags:** #action

### pre_get_product_search_form
**Tags:** #action

### woocommerce_$PRODUCT->GET_TYPE_add_to_cart
**Tags:** #action

### product_variation_linked
**Args:** $variation_id
**Tags:** #action

### woocommerce_before_delete_product_variation
**Params:** int $variation_id
**Since:** 3.0.0 | **Tags:** #action
Fires before a product variation is permanently deleted.

### woocommerce_coupon_loaded
**Args:** $coupon
**Tags:** #action

### woocommerce_coupon_object_updated_props
**Args:** $coupon, $this->updated_props
**Tags:** #action

### woocommerce_decrease_coupon_usage_count
**Args:** $coupon, $new_count, $used_by
**Tags:** #action

### woocommerce_delete_coupon
**Args:** $id
**Tags:** #action

### woocommerce_delete_product_variation
**Params:** int $variation_id
**Since:** 3.0.0 | **Tags:** #action
Fires after a product variation has been permanently deleted.

### woocommerce_downloadable_product_download_log_insert
**Args:** $data
**Tags:** #action

### woocommerce_grant_product_download_access
**Args:** $data
**Tags:** #action

### woocommerce_increase_coupon_usage_count
**Args:** $coupon, $new_count, $used_by
**Tags:** #action

### woocommerce_new_coupon
**Args:** $coupon_id, $coupon
**Tags:** #action

### woocommerce_new_product
**Args:** $id, $product
**Tags:** #action

### woocommerce_new_product_variation
**Args:** $id, $product
**Tags:** #action

### woocommerce_process_product_file_download_paths
**Args:** $product->get_parent_id(), $product->get_id(), $downloads
**Tags:** #action

### woocommerce_product_attributes_updated
**Params:** WC_Product $product, bool $force
**Since:** 10.2.0 | **Tags:** #action
Fires after WooCommerce product attributes have been updated.

### woocommerce_product_before_set_stock
**Params:** int $product
**Since:** 4.9 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a product is about to change.

### woocommerce_product_object_updated_props
**Args:** $product, $this->updated_props
**Tags:** #action

### woocommerce_product_read
**Params:** int $product_id, WC_Product $product
**Since:** 3.7.0 | **Tags:** #action
Fires when a product is read into memory.

### woocommerce_product_set_stock
**Params:** WC_Product $product
**Since:** 3.0 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a product has changed.

### woocommerce_product_set_stock_status
**Params:** int $product_id, string $stock_status, WC_Product $product
**Since:** 3.0 | **Tags:** #action
Action to signal that the `stock_status` for a product has changed.

### woocommerce_product_set_visibility
**Args:** $product->get_id(), $product->get_catalog_visibility()
**Tags:** #action

### woocommerce_product_type_changed
**Args:** $product, $old_type, $new_type
**Tags:** #action

### woocommerce_trash_coupon
**Args:** $id
**Tags:** #action

### woocommerce_trash_product_variation
**Params:** int $variation_id
**Since:** 3.0.0 | **Tags:** #action
Fires after a product variation has been trashed.

### woocommerce_update_coupon
**Args:** $coupon->get_id(), $coupon
**Tags:** #action

### woocommerce_update_product
**Args:** $product->get_id(), $product
**Tags:** #action

### woocommerce_update_product_variation
**Args:** $product->get_id(), $product
**Tags:** #action

### woocommerce_updated_product_price
**Params:** int $product_id
**Since:** 3.6 | **Tags:** #action
Fire an action for this direct update so it can be detected by other code.

### woocommerce_updated_product_sales
**Params:** int $product_id
**Since:** 3.6 | **Tags:** #action
Fire an action for this direct update so it can be detected by other code.

### woocommerce_updated_product_stock
**Params:** int $product_id_with_stock
**Since:** 3.6 | **Tags:** #action
Fire an action for this direct update so it can be detected by other code.

### woocommerce_variation_before_set_stock
**Params:** int $product
**Since:** 4.9 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a variation is about to change.

### woocommerce_variation_set_stock
**Params:** WC_Product $product
**Since:** 3.0 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a variation has changed.

### woocommerce_variation_set_stock_status
**Params:** int $product_id, string $stock_status, WC_Product $product
**Since:** 3.0 | **Tags:** #action
Action to signal that the `stock_status` for a variation has changed.

### wc_after_products_ending_sales
**Args:** $product_ids
**Tags:** #action

### wc_after_products_starting_sales
**Args:** $product_ids
**Tags:** #action

### wc_before_products_ending_sales
**Args:** $product_ids
**Tags:** #action

### wc_before_products_starting_sales
**Args:** $product_ids
**Tags:** #action

### woocommerce_$PRODUCT_TYPE_add_to_cart
**Tags:** #action

### woocommerce_add_to_cart
**Params:** string $cart_id, integer $product_id, integer $request_quantity, integer $variation_id, array $variation, array $cart_item_data
**Since:** 2.5.0 | **Tags:** #action
Fires when an item is added to the cart. This hook fires when an item is added to the cart. This is triggered from the Store API in this context, but WooCommerce core add to cart events trigger the same hook.

### woocommerce_after_product_attribute_settings
**Params:** WC_Product_Attribute $attribute, int $i
**Since:** 3.4.0 | **Tags:** #action
Hook to display custom attribute terms.

### woocommerce_after_product_ordering
**Args:** $sorting_id, $menu_orders
**Tags:** #action

### woocommerce_after_single_product_ordering
**Args:** $id, $index
**Tags:** #action

### woocommerce_ajax_revoke_access_to_product_download
**Args:** $download_id, $product_id, $order_id, $permission_id
**Tags:** #action

### woocommerce_ajax_save_product_variations
**Args:** $product_id
**Tags:** #action

### woocommerce_analytics_delete_coupon
**Params:** int $coupon_id, int $order_id
**Tags:** #action
Fires when coupon's reports are removed from database.

### woocommerce_analytics_delete_product
**Params:** int $product_id, int $order_id
**Tags:** #action
Fires when product's reports are removed from database.

### woocommerce_analytics_update_coupon
**Params:** int $coupon_id, int $order_id
**Tags:** #action
Fires when coupon's reports are updated.

### woocommerce_analytics_update_product
**Params:** int $order_item_id, int $order_id
**Tags:** #action
Fires when product's reports are updated.

### woocommerce_applied_coupon
**Params:** string $coupon_code
**Since:** 2.0.0 | **Tags:** #action
Action ran after a coupon is applied.

### woocommerce_before_calculate_totals
**Args:** $this
**Tags:** #action

### woocommerce_bulk_edit_variations
**Args:** $bulk_action, $data, $product_id, $variations
**Tags:** #action

### woocommerce_bulk_edit_variations_default
**Args:** $bulk_action, $data, $product_id, $variations
**Tags:** #action

### woocommerce_coupon_data_panels
**Args:** $coupon->get_id(), $coupon
**Tags:** #action

### woocommerce_coupon_options
**Args:** $coupon->get_id(), $coupon
**Tags:** #action

### woocommerce_coupon_options_save
**Args:** $post_id, $coupon
**Tags:** #action

### woocommerce_coupon_options_usage_limit
**Args:** $coupon->get_id(), $coupon
**Tags:** #action

### woocommerce_coupon_options_usage_restriction
**Args:** $coupon->get_id(), $coupon
**Tags:** #action

### woocommerce_delete_product_transients
**Params:** int $product_id
**Since:** 2.3.0 | **Tags:** #action
Fires after product transients are deleted.

### woocommerce_grant_product_download_permissions
**Args:** $order_id
**Tags:** #action

### woocommerce_helper_subscription_activate_error
**Params:** int $product_id, string $product_key, array $activation_response
**Tags:** #action
Fires when the Helper fails to activate a product.

### woocommerce_helper_subscription_activate_success
**Params:** int $product_id, string $product_key, array $activation_response
**Tags:** #action
Fires when the Helper activates a product successfully.

### woocommerce_helper_subscription_deactivate_error
**Params:** int $product_id, string $product_key, array $deactivation_response
**Tags:** #action
Fires when the Helper fails to activate a product.

### woocommerce_helper_subscription_deactivate_success
**Params:** int $product_id, string $product_key, array $deactivation_response
**Tags:** #action
Fires when the Helper activates a product successfully.

### woocommerce_helper_subscriptions_refresh
8.3.0
**Since:** Fires when Helper subscriptions are refreshed. | **Tags:** #action

### woocommerce_low_stock
**Params:** int $product
**Since:** 4.9 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a product is about to change.

### woocommerce_no_stock
**Params:** int $product
**Since:** 4.9 | **Tags:** #action
Action to signal that the value of 'stock_quantity' for a variation is about to change.

### woocommerce_process_product_meta_$PRODUCT_TYPE
**Tags:** #action

### woocommerce_product_after_variable_attributes
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options download action.

### woocommerce_product_bulk_and_quick_edit
**Args:** $post_id, $post
**Tags:** #action

### woocommerce_product_bulk_edit_end
**Tags:** #action

### woocommerce_product_bulk_edit_save
**Args:** $product
**Tags:** #action

### woocommerce_product_bulk_edit_start
**Tags:** #action

### woocommerce_product_data_panels
**Tags:** #action

### woocommerce_product_duplicate
**Args:** $duplicate, $product
**Tags:** #action

### woocommerce_product_duplicate_before_save
**Args:** $duplicate, $product
**Tags:** #action

### woocommerce_product_export_row
**Tags:** #action

### woocommerce_product_import_before_import
**Args:** $parsed_data
**Tags:** #action

### woocommerce_product_import_before_process_item
**Params:** array $data
**Tags:** #action
Process a single item and save.

### woocommerce_product_import_inserted_product_object
**Args:** $object, $data
**Tags:** #action

### woocommerce_product_importer_before_set_parsed_data
**Args:** $row, $mapped_keys
**Tags:** #action

### woocommerce_product_on_backorder
**Params:** array $args
**Since:** 3.0 | **Tags:** #action
Action fires when an item in an order is backordered.

### woocommerce_product_option_terms
**Params:** array|null $attribute_taxonomy, int $i, WC_Product_Attribute $attribute
**Since:** 3.4.0 | **Tags:** #action
Hook to display custom attribute terms.

### woocommerce_product_options_advanced
**Tags:** #action

### woocommerce_product_options_attributes
**Tags:** #action

### woocommerce_product_options_dimensions
**Tags:** #action

### woocommerce_product_options_downloads
**Tags:** #action

### woocommerce_product_options_external
**Tags:** #action

### woocommerce_product_options_general_product_data
**Tags:** #action

### woocommerce_product_options_global_unique_id
**Tags:** #action

### woocommerce_product_options_inventory_product_data
**Tags:** #action

### woocommerce_product_options_pricing
**Tags:** #action

### woocommerce_product_options_related
**Tags:** #action

### woocommerce_product_options_reviews
**Tags:** #action

### woocommerce_product_options_shipping
**Tags:** #action

### woocommerce_product_options_shipping_product_data
**Tags:** #action

### woocommerce_product_options_sku
**Tags:** #action

### woocommerce_product_options_sold_individually
**Tags:** #action

### woocommerce_product_options_stock
**Tags:** #action

### woocommerce_product_options_stock_fields
**Tags:** #action

### woocommerce_product_options_stock_status
**Tags:** #action

### woocommerce_product_options_tax
**Tags:** #action

### woocommerce_product_query
**Args:** $q, $this
**Tags:** #action

### woocommerce_product_quick_edit_end
**Tags:** #action

### woocommerce_product_quick_edit_save
**Args:** $product
**Tags:** #action

### woocommerce_product_quick_edit_start
**Tags:** #action

### woocommerce_product_reviews_table_column_$COLUMN_NAME
**Tags:** #action

### woocommerce_product_write_panel_tabs
**Tags:** #action

### woocommerce_recorded_sales
**Params:** int $order_id
**Tags:** #action
Called when sales for an order are recorded

### woocommerce_removed_coupon
**Args:** $coupon_code
**Tags:** #action

### woocommerce_save_product_variation
**Params:** object $variation, int $i
**Since:** 3.8.0 | **Tags:** #action
Set variation props before save.

### woocommerce_store_api_validate_add_to_cart
**Params:** \WC_Product $product, array $request
**Since:** 7.1.0 | **Tags:** #action
Fires during validation when adding an item to the cart via the Store API. Fire action to validate add to cart. Functions hooking into this should throw an \Exception to prevent add to cart from happening.

### woocommerce_updated_product_attribute_summary
**Params:** int $variation_id
**Since:** 10.2.0 | **Tags:** #action
Fires after the attribute summary of a product variation has been updated.

### woocommerce_variable_product_before_variations
**Tags:** #action

### woocommerce_variable_product_bulk_edit_actions
**Tags:** #action

### woocommerce_variable_product_sync_data
**Args:** $product
**Tags:** #action

### woocommerce_variation_header
**Params:** WP_Post $variation, int $loop
**Since:** 3.6.0 | **Tags:** #action
Variations header action.

### woocommerce_variation_options
**Args:** $loop, $variation_data, $variation
**Tags:** #action

### woocommerce_variation_options_dimensions
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options dimensions action.

### woocommerce_variation_options_download
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options download action.

### woocommerce_variation_options_inventory
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options inventory action.

### woocommerce_variation_options_pricing
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options pricing action.

### woocommerce_variation_options_tax
**Params:** int $loop, array $variation_data, WP_Post $variation
**Since:** 2.5.0 | **Tags:** #action
Variation options tax action.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
