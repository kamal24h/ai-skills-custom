# WooCommerce Actions: Checkout

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_checkout_billing_form
**Args:** $checkout
**Tags:** #action

### woocommerce_after_checkout_form
**Args:** $checkout
**Tags:** #action

### woocommerce_after_checkout_registration_form
**Args:** $checkout
**Tags:** #action

### woocommerce_after_checkout_shipping_form
**Args:** $checkout
**Tags:** #action

### woocommerce_before_checkout_billing_form
**Args:** $checkout
**Tags:** #action

### woocommerce_before_checkout_form
**Args:** $checkout
**Tags:** #action

### woocommerce_before_checkout_registration_form
**Args:** $checkout
**Tags:** #action

### woocommerce_before_checkout_shipping_form
**Args:** $checkout
**Tags:** #action

### woocommerce_checkout_after_customer_details
**Tags:** #action

### woocommerce_checkout_after_order_review
**Tags:** #action

### woocommerce_checkout_after_terms_and_conditions
**Tags:** #action

### woocommerce_checkout_before_customer_details
**Tags:** #action

### woocommerce_checkout_before_order_review
**Tags:** #action

### woocommerce_checkout_before_order_review_heading
**Tags:** #action

### woocommerce_checkout_before_terms_and_conditions
**Tags:** #action

### woocommerce_checkout_billing
**Tags:** #action

### woocommerce_checkout_order_review
**Tags:** #action

### woocommerce_checkout_shipping
**Tags:** #action

### woocommerce_checkout_terms_and_conditions
**Tags:** #action

### woocommerce_proceed_to_checkout
**Tags:** #action

### woocommerce_before_checkout_form_cart_notices
**Tags:** #action

### woocommerce_after_checkout_validation
**Args:** $data, $errors
**Tags:** #action

### woocommerce_before_checkout_process
**Tags:** #action

### woocommerce_blocks_checkout_enqueue_data
2.6.0
**Since:** Fires after checkout block data is registered. | **Tags:** #action

### woocommerce_blocks_enqueue_checkout_block_scripts_after
4.6.0
**Since:** Fires after checkout block scripts are enqueued. | **Tags:** #action

### woocommerce_blocks_enqueue_checkout_block_scripts_before
4.6.0
**Since:** Fires before checkout block scripts are enqueued. | **Tags:** #action

### woocommerce_checkout_create_order
**Args:** $order, $data
**Tags:** #action

### woocommerce_checkout_create_order_coupon_item
**Args:** $item, $code, $coupon, $order
**Tags:** #action

### woocommerce_checkout_create_order_fee_item
**Args:** $item, $fee_key, $fee, $order
**Tags:** #action

### woocommerce_checkout_create_order_line_item
**Args:** $item, $cart_item_key, $values, $order
**Tags:** #action

### woocommerce_checkout_create_order_shipping_item
**Args:** $item, $package_key, $package, $order
**Tags:** #action

### woocommerce_checkout_create_order_tax_item
**Args:** $item, $tax_rate_id, $order
**Tags:** #action

### woocommerce_checkout_init
**Args:** self::$instance
**Tags:** #action

### woocommerce_checkout_order_created
**Args:** $order
**Tags:** #action

### woocommerce_checkout_order_exception
**Args:** $order
**Tags:** #action

### woocommerce_checkout_order_processed
**Args:** $order_id, $posted_data, $order
**Tags:** #action

### woocommerce_checkout_process
**Tags:** #action

### woocommerce_checkout_update_customer
**Args:** $customer, $data
**Tags:** #action

### woocommerce_checkout_update_order_meta
**Args:** $order_id, $data
**Tags:** #action

### woocommerce_checkout_update_order_review
**Args:** isset( $_POST['post_data'] ) ? wp_unslash( $_POST['post_data'] ) : ''
**Tags:** #action

### woocommerce_checkout_update_user_meta
**Args:** $customer_id, $data
**Tags:** #action

### woocommerce_checkout_validate_order_before_payment
**Params:** \WC_Order $order, \WP_Error $validation_errors
**Since:** 9.9.0 | **Tags:** #action
Allow plugins to perform custom validation before payment. Plugins can add errors to the $validation_errors object.

### woocommerce_store_api_checkout_order_processed
**Params:** \WC_Order $order
**Since:** 7.2.0 | **Tags:** #action
Fires before an order is processed by the Checkout Block/Store API. This hook informs extensions that $order has completed processing and is ready for payment. This is similar to existing core hook woocommerce_checkout_order_processed. We're using a new action: - To keep the interface focused (only pass $order, not passing request data). - This also explicitly indicates these orders are from checkout block/StoreAPI.

### woocommerce_store_api_checkout_update_customer_from_request
**Params:** \WC_Customer $customer, \WP_REST_Request $request
**Since:** 8.2.0 | **Tags:** #action
Fires when the Checkout Block/Store API updates a customer from the API request data.

### woocommerce_store_api_checkout_update_order_from_request
**Params:** \WC_Order $order, \WP_REST_Request $request
**Since:** 7.2.0 | **Tags:** #action
Fires when the Checkout Block/Store API updates an order's from the API request data. This hook gives extensions the chance to update orders based on the data in the request. This can be used in conjunction with the ExtendSchema class to post custom data and then process it.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
