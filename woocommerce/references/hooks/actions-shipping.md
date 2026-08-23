# WooCommerce Actions: Shipping

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_shipping_calculator
**Tags:** #action

### woocommerce_after_shipping_rate
**Args:** $method, $index
**Tags:** #action

### woocommerce_before_shipping_calculator
**Tags:** #action

### woocommerce_review_order_after_shipping
**Tags:** #action

### woocommerce_review_order_before_shipping
**Tags:** #action

### woocommerce_calculated_shipping
**Tags:** #action

### woocommerce_delete_shipping_zone
**Args:** $zone_id
**Tags:** #action

### woocommerce_delete_shipping_zone_method
**Args:** $instance_id
**Tags:** #action

### woocommerce_shipping_zone_loaded
**Params:** WC_Shipping_Zone $zone
**Tags:** #action
Indicate that the WooCommerce shipping zone has been loaded.

### woocommerce_$THIS->ID_shipping_add_rate
**Tags:** #action

### woocommerce_flat_rate_shipping_add_rate
**Args:** $this, $rate
**Tags:** #action

### woocommerce_load_shipping_methods
**Args:** $package
**Tags:** #action

### woocommerce_shipping_classes_column_$CLASS
**Tags:** #action

### woocommerce_shipping_classes_save_class
**Args:** $term_id, $data
**Tags:** #action

### woocommerce_shipping_init
**Tags:** #action

### woocommerce_shipping_method_chosen
**Params:** string $chosen_method
**Since:** 3.2.0 | **Tags:** #action
Fires when a shipping method is chosen.

### woocommerce_shipping_providers_column_$CLASS
**Tags:** #action

### woocommerce_shipping_zone_after_methods_table
**Args:** $zone
**Tags:** #action

### woocommerce_shipping_zone_before_methods_table
**Args:** $zone
**Tags:** #action

### woocommerce_shipping_zone_method_added
**Args:** $instance_id, $type, $this->get_id()
**Tags:** #action

### woocommerce_shipping_zone_method_deleted
**Args:** $instance_id, $method_id, $zone_id
**Tags:** #action

### woocommerce_shipping_zone_method_status_toggled
**Params:** int $instance_id, string $method_id, int $zone_id, bool $is_enabled
**Since:** 3.0.0 | **Tags:** #action
Fires when a shipping method's enabled status is toggled.

### woocommerce_store_api_cart_select_shipping_rate
**Params:** string|null $package_id, string $rate_id, \WP_REST_Request $request
**Since:** 9.0.0 | **Tags:** #action
Fires an action after a shipping method has been chosen for package(s) via the Store API. This allows extensions to perform addition actions after a shipping method has been chosen, but before the cart totals are recalculated.

### woocommerce_webhook_delivery
**Args:** $http_args, $response, $duration, $arg, $this->get_id()
**Tags:** #action

### woocommerce_webhook_disabled_due_delivery_failures
**Args:** $this->get_id()
**Tags:** #action

### woocommerce_webhook_process_delivery
**Args:** $this, $arg
**Tags:** #action

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
