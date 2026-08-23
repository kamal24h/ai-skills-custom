# WooCommerce Filters: Checkout

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_checkout_cart_item_quantity
**Args:** ' <strong class="product-quantity">' . sprintf( '&times;&nbsp;%s', $cart_item['quantity'] ) . '</strong>', $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_checkout_cart_item_visible
**Params:** bool $visible, array $cart_item, string $cart_item_key
**Since:** 2.1.0 | **Tags:** #filter
Filter whether this cart item is visible in the checkout review order table.

### woocommerce_checkout_coupon_message
**Params:** string $message
**Since:** 1.0.0 | **Tags:** #filter
Filter checkout coupon message.

### woocommerce_checkout_login_message
**Args:** esc_html__( 'Returning customer?', 'woocommerce' )
**Tags:** #filter

### woocommerce_checkout_must_be_logged_in_message
**Params:** string $message
**Since:** 9.4.3 | **Tags:** #filter
Filter to customize the checkout message when a user must be logged in.

### woocommerce_checkout_show_terms
**Args:** true
**Tags:** #filter

### woocommerce_enable_order_notes_field
**Args:** 'yes' === get_option( 'woocommerce_enable_order_comments', 'yes' )
**Tags:** #filter

### woocommerce_checkout_redirect_empty_cart
**Args:** true
**Tags:** #filter

### default_checkout_$INPUT
**Tags:** #filter

### woocommerce_checkout_create_order_line_item_object
**Args:** new WC_Order_Item_Product(), $cart_item_key, $values, $order
**Tags:** #filter

### woocommerce_checkout_customer_id
**Args:** get_current_user_id()
**Tags:** #filter

### woocommerce_checkout_fields
**Params:** array[] $checkout_fields
**Since:** 3.0.0 | **Tags:** #filter
Sets the fields used during checkout.

### woocommerce_checkout_get_value
**Args:** null, $input
**Tags:** #filter

### woocommerce_checkout_no_payment_needed_redirect
**Args:** $order->get_checkout_order_received_url(), $order
**Tags:** #filter

### woocommerce_checkout_postcode_validation_notice
**Args:** $postcode_validation_notice, $country, $data[ $key ]
**Tags:** #filter

### woocommerce_checkout_posted_data
**Args:** $data
**Tags:** #filter

### woocommerce_checkout_registration_enabled
**Params:** bool $checkout_registration_enabled
**Since:** 3.0.0 | **Tags:** #filter
Determines if customer registration is enabled during checkout.

### woocommerce_checkout_registration_required
**Params:** bool $checkout_registration_required
**Since:** 3.0.0 | **Tags:** #filter
Controls if registration is required in order for checkout to be completed.

### woocommerce_checkout_required_field_notice
**Args:** sprintf( __( '%s is a required field.', 'woocommerce' ), '<strong>' . esc_html( $field_label ) . '</strong>' ), $field_label, $key
**Tags:** #filter

### woocommerce_checkout_update_customer_data
**Args:** true, $this
**Tags:** #filter

### woocommerce_checkout_update_order_review_expired
**Args:** true
**Tags:** #filter

### woocommerce_enforce_password_strength_meter_on_checkout
**Args:** false
**Tags:** #filter

### woocommerce_force_ssl_checkout
**Args:** false
**Tags:** #filter

### woocommerce_get_checkout_order_received_url
**Args:** $order_received_url, $this
**Tags:** #filter

### woocommerce_get_checkout_payment_url
**Args:** $pay_url, $this
**Tags:** #filter

### woocommerce_get_checkout_url
**Args:** $checkout_url
**Tags:** #filter

### woocommerce_hold_stock_for_checkout
**Params:** bool $enabled
**Since:** 4.3.0 | **Tags:** #filter
Filter: woocommerce_hold_stock_for_checkout Allows enable/disable hold stock functionality on checkout.

### woocommerce_is_checkout
**Params:** bool $is_checkout
**Since:** 2.4.0 | **Tags:** #filter
Filter to allow for custom logic to determine if the checkout page is being viewed.

### woocommerce_process_checkout_$TYPE_field
**Tags:** #filter

### woocommerce_process_checkout_field_$KEY
**Tags:** #filter

### woocommerce_unforce_ssl_checkout
**Args:** true
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
