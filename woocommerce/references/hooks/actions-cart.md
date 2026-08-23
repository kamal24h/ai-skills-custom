# WooCommerce Actions: Cart

> Core WooCommerce action hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_after_cart
**Tags:** #action

### woocommerce_after_cart_contents
**Tags:** #action

### woocommerce_after_cart_item_name
**Args:** $cart_item, $cart_item_key
**Tags:** #action

### woocommerce_after_cart_table
**Tags:** #action

### woocommerce_after_cart_totals
**Tags:** #action

### woocommerce_before_cart
**Tags:** #action

### woocommerce_before_cart_collaterals
**Tags:** #action

### woocommerce_before_cart_contents
**Tags:** #action

### woocommerce_before_cart_table
**Tags:** #action

### woocommerce_before_cart_totals
**Tags:** #action

### woocommerce_before_mini_cart_contents
**Tags:** #action

### woocommerce_cart_actions
**Tags:** #action

### woocommerce_cart_collaterals
**Tags:** #action

### woocommerce_cart_contents
**Tags:** #action

### woocommerce_cart_coupon
**Tags:** #action

### woocommerce_cart_has_errors
**Tags:** #action

### woocommerce_cart_is_empty
**Tags:** #action

### woocommerce_cart_totals_after_order_total
**Tags:** #action

### woocommerce_cart_totals_after_shipping
**Tags:** #action

### woocommerce_cart_totals_before_order_total
**Tags:** #action

### woocommerce_cart_totals_before_shipping
**Tags:** #action

### woocommerce_mini_cart_contents
**Tags:** #action

### woocommerce_review_order_after_cart_contents
**Tags:** #action

### woocommerce_review_order_before_cart_contents
**Tags:** #action

### woocommerce_widget_shopping_cart_after_buttons
**Tags:** #action

### woocommerce_widget_shopping_cart_before_buttons
**Tags:** #action

### woocommerce_widget_shopping_cart_buttons
**Tags:** #action

### woocommerce_widget_shopping_cart_total
**Tags:** #action

### woocommerce_check_cart_items
7.2.0
**Since:** Fires when cart items are being validated. Allow 3rd parties to validate cart items. This is a legacy hook from Woo core. This filter will be deprecated because it encourages usage of wc_add_notice. For the API we need to capture notices and convert to wp errors instead. | **Tags:** #action

### internal_woocommerce_cart_item_added_from_user_request
**Params:** int $product_id, int|float $quantity
**Since:** 10.6.0 | **Tags:** #action
Fires when an item is added to the cart from a user request.

### internal_woocommerce_cart_item_removed_from_user_request
**Params:** string $cart_item_key, \WC_Cart $cart
**Since:** 10.6.0 | **Tags:** #action
Fires when an item is removed from the cart from a user request.

### internal_woocommerce_cart_item_updated_from_user_request
**Params:** string $cart_item_key, int|float $quantity, int|float $old_quantity, \WC_Cart $cart
**Since:** 10.6.0 | **Tags:** #action
Fires when a cart item quantity is updated from a user request.

### woocommerce_add_to_cart_handler_$ADD_TO_CART_HANDLER
**Tags:** #action

### woocommerce_after_cart_item_quantity_update
**Args:** $cart_item_key, $quantity, $old_quantity, $this
**Tags:** #action

### woocommerce_ajax_added_to_cart
**Args:** $product_id
**Tags:** #action

### woocommerce_before_cart_emptied
**Params:** bool $clear_persistent_cart
**Since:** 9.7.0 | **Tags:** #action
Fires before the cart is emptied.

### woocommerce_blocks_cart_enqueue_data
2.6.0
**Since:** Fires after cart block data is registered. | **Tags:** #action

### woocommerce_blocks_enqueue_cart_block_scripts_after
2.6.0
**Since:** Fires after cart block scripts are enqueued. | **Tags:** #action

### woocommerce_blocks_enqueue_cart_block_scripts_before
2.6.0
**Since:** Fires before cart block scripts are enqueued. | **Tags:** #action

### woocommerce_calculate_totals
**Args:** $this->cart
**Tags:** #action

### woocommerce_cart_calculate_fees
**Args:** $this
**Tags:** #action

### woocommerce_cart_emptied
**Params:** bool $clear_persistent_cart
**Since:** 9.7.0 | **Tags:** #action
Fires after the cart is emptied.

### woocommerce_cart_item_removed
**Args:** $cart_item_key, $this
**Tags:** #action

### woocommerce_cart_item_restored
**Args:** $cart_item_key, $this
**Tags:** #action

### woocommerce_cart_item_set_quantity
**Params:** string $cart_item_key, int $quantity, WC_Cart $this
**Since:** 3.6.0 | **Tags:** #action
Fired after qty has been changed.

### woocommerce_cart_loaded_from_session
**Params:** WC_Cart $cart
**Since:** 3.2.0 | **Tags:** #action
Fires when cart is loaded from session.

### woocommerce_cart_reset
**Args:** $this, false
**Tags:** #action

### woocommerce_cart_updated
3.2.0
**Since:** Fires when cart is updated. | **Tags:** #action

### woocommerce_remove_cart_item
**Args:** $cart_item_key, $this
**Tags:** #action

### woocommerce_remove_cart_item_from_session
**Params:** string $key, array $values, WC_Product $product
**Since:** 3.6.0 | **Tags:** #action
Fires when cart item is removed from the session.

### woocommerce_set_cart_cookies
**Args:** $set
**Tags:** #action

### woocommerce_store_api_cart_errors
**Params:** \WP_Error $errors, \WC_Cart $cart
**Since:** 7.2.0 | **Tags:** #action
Fires an action to validate the cart. Functions hooking into this should add custom errors using the provided WP_Error instance.

### woocommerce_store_api_validate_cart_item
**Params:** \WC_Product $product, array $cart_item
**Since:** 7.1.0 | **Tags:** #action
Fire action to validate add to cart. Functions hooking into this should throw an \Exception to prevent add to cart from occurring.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
