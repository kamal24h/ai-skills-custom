# WooCommerce Filters: Cart

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_cart_item_backorder_notification
**Args:** '<p class="backorder_notification">' . esc_html__( 'Available on backorder', 'woocommerce' ) . '</p>', $product_id
**Tags:** #filter

### woocommerce_cart_item_class
**Args:** 'cart_item', $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_cart_item_name
**Params:** string $product_name, array $cart_item, string $cart_item_key
**Since:** 2.1.0 | **Tags:** #filter
Filter the product name.

### woocommerce_cart_item_permalink
**Params:** string $product_permalink, array $cart_item, string $cart_item_key
**Since:** 9.9.0 | **Tags:** #filter
Filter the product permalink. This is a hook taken from the legacy cart/mini-cart templates that allows the permalink to be changed for a product. This is specific to the cart endpoint.

### woocommerce_cart_item_price
**Args:** WC()->cart->get_product_price( $_product ), $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_cart_item_product
**Args:** $cart_item['data'], $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_cart_item_product_id
**Args:** $cart_item['product_id'], $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_cart_item_quantity
**Args:** $product_quantity, $cart_item_key, $cart_item
**Tags:** #filter

### woocommerce_cart_item_remove_link
**Tags:** #filter

### woocommerce_cart_item_subtotal
**Args:** WC()->cart->get_product_subtotal( $_product, $cart_item['quantity'] ), $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_cart_item_thumbnail
**Params:** string $thumbnail, array $cart_item, string $cart_item_key
**Since:** 2.1.0 | **Tags:** #filter
Filter the product thumbnail displayed in the WooCommerce cart. This filter allows developers to customize the HTML output of the product thumbnail. It passes the product image along with cart item data for potential modifications before being displayed in the cart.

### woocommerce_cart_item_visible
**Params:** bool $visible, array $cart_item, string $cart_item_key
**Since:** 2.1.0 | **Tags:** #filter
Filter whether this cart item is visible in the cart.

### woocommerce_loop_add_to_cart_link
**Params:** string $class
**Since:** 8.7.0 | **Tags:** #filter
Filters the add to cart button class.

### woocommerce_mini_cart_item_class
**Args:** 'mini_cart_item', $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_widget_cart_item_quantity
**Args:** '<span class="quantity">' . sprintf( '%s &times; %s', $cart_item['quantity'], $product_price ) . '</span>', $cart_item, $cart_item_key
**Tags:** #filter

### woocommerce_widget_cart_item_visible
**Params:** bool $visible, array $cart_item, string $cart_item_key
**Since:** 1.6.0 | **Tags:** #filter
Filter whether this cart item is visible in the mini-cart.

### wc_empty_cart_message
**Params:** string $message
**Since:** 3.1.0 | **Tags:** #filter
Filter empty cart message text.

### woocommerce_loop_add_to_cart_args
**Params:** array $args
**Since:** 2.4.11 | **Tags:** #filter
Filter to customize the arguments for the add to cart template for the loop.

### woocommerce_cart_calculate_shipping_address
**Args:** $address
**Tags:** #filter

### woocommerce_output_cart_shortcode_content
**Params:** array $atts
**Tags:** #filter
Output the cart shortcode.

### woocommerce_widget_cart_is_hidden
**Params:** array $args, array $instance
**Tags:** #filter
Output widget.

### wc_add_to_cart_message
**Args:** $message, $product_id
**Tags:** #filter

### wc_add_to_cart_message_html
**Args:** $message, $products, $show_qty
**Tags:** #filter

### woocommerce_add_cart_item
**Params:** array $cart_item_data, string $cart_id
**Since:** 2.5.0 | **Tags:** #filter
Filters the item being added to the cart.

### woocommerce_add_cart_item_data
**Args:** $cart_item_data, $product_id, $variation_id, $quantity
**Tags:** #filter

### woocommerce_add_order_again_cart_item
**Args:** array_merge(
					$cart_item_data,
					array(
						'key'          => $cart_id,
						'product_id'   => $product_id,
						'variation_id' => $variation_id,
						'variation'    => $variations,
						'quantity'     => $quantity,
						'data'         => $product_data,
						'data_hash'    => wc_get_cart_item_data_hash( $product_data ),
					)
				), $cart_id
**Tags:** #filter

### woocommerce_add_to_cart_fragments
**Args:** array(
					'div.widget_shopping_cart_content' => '<div class="widget_shopping_cart_content">' . $mini_cart . '</div>',
				)
**Tags:** #filter

### woocommerce_add_to_cart_handler
**Args:** $adding_to_cart->get_type(), $adding_to_cart
**Tags:** #filter

### woocommerce_add_to_cart_item_name_in_quotes
**Params:** string $item_name_in_quotes, int $product_id
**Since:** 2.6.1 | **Tags:** #filter
Filters the item name in quotes for the add to cart message.

### woocommerce_add_to_cart_notice_type
**Args:** 'success'
**Tags:** #filter

### woocommerce_add_to_cart_qty_html
**Params:** string $qty_html, int $product_id
**Since:** 2.6.1 | **Tags:** #filter
Filters the quantity HTML for the add to cart message.

### woocommerce_add_to_cart_quantity
**Params:** number $quantity, number $product_id, number $variation_id
**Since:** 3.1.0 | **Tags:** #filter
Filters the change the quantity to add to cart.

### woocommerce_add_to_cart_redirect
**Args:** $url, $adding_to_cart
**Tags:** #filter

### woocommerce_add_to_cart_sold_individually_found_in_cart
**Args:** isset( $cart[ $cart_id ] ) && isset( $cart[ $cart_id ]['quantity'] ) && $cart[ $cart_id ]['quantity'] > 0, $product_id, $variation_id, $cart_item_data, $cart_id
**Tags:** #filter

### woocommerce_add_to_cart_sold_individually_quantity
**Args:** 1, $quantity, $product_id, $variation_id, $cart_item_data
**Tags:** #filter

### woocommerce_add_to_cart_validation
**Params:** boolean $passed_validation, integer $product_id, integer $quantity, integer $variation_id, array $variation
**Since:** 7.2.0 | **Tags:** #filter
Filters if an item being added to the cart passed validation checks. Allow 3rd parties to validate if an item can be added to the cart. This is a legacy hook from Woo core. This filter will be deprecated because it encourages usage of wc_add_notice. For the API we need to capture notices and convert to exceptions instead.

### woocommerce_cart___FUNCTION__
**Tags:** #filter

### woocommerce_cart_contents_changed
**Params:** array $cart_contents
**Since:** 3.2.0 | **Tags:** #filter
Filter the cart contents.

### woocommerce_cart_contents_count
**Args:** array_sum( wp_list_pluck( $this->get_cart(), 'quantity' ) )
**Tags:** #filter

### woocommerce_cart_contents_total
**Args:** wc_price( wc_prices_include_tax() ? $this->get_cart_contents_total() + $this->get_cart_contents_tax() : $this->get_cart_contents_total() )
**Tags:** #filter

### woocommerce_cart_contents_weight
**Args:** $weight
**Tags:** #filter

### woocommerce_cart_coupon_types
**Args:** array( 'fixed_cart' )
**Tags:** #filter

### woocommerce_cart_crosssell_ids
**Args:** wp_parse_id_list( $cross_sells ), $this
**Tags:** #filter

### woocommerce_cart_discounts_before_tax
**Args:** $discounts_before_tax, $this
**Tags:** #filter

### woocommerce_cart_fragment_name
**Args:** 'wc_fragments_' . md5( get_current_blog_id() . '_' . get_site_url( get_current_blog_id(), '/' ) . get_template() )
**Tags:** #filter

### woocommerce_cart_get_taxes
**Args:** wc_array_merge_recursive_numeric( $this->get_shipping_taxes(), $this->get_cart_contents_taxes(), $this->get_fee_taxes() ), $this
**Tags:** #filter

### woocommerce_cart_hash
**Args:** $hash, $cart_session
**Tags:** #filter

### woocommerce_cart_hash_key
**Args:** 'wc_cart_hash_' . md5( get_current_blog_id() . '_' . get_site_url( get_current_blog_id(), '/' ) . get_template() )
**Tags:** #filter

### woocommerce_cart_hide_zero_taxes
**Args:** true
**Tags:** #filter

### woocommerce_cart_id
**Args:** md5( implode( '_', $id_parts ) ), $product_id, $variation_id, $variation, $cart_item_data
**Tags:** #filter

### woocommerce_cart_item_data_to_validate
**Params:** WC_Product $product
**Tags:** #filter
Gets a hash of important product data that when changed should cause cart items to be invalidated. The woocommerce_cart_item_data_to_validate filter can be used to add custom properties.

### woocommerce_cart_item_is_purchasable
**Params:** bool $is_purchasable, string $key, array $values, WC_Product $product
**Since:** 7.0.0 | **Tags:** #filter
Allow 3rd parties to override this item's is_purchasable() result with cart item data.

### woocommerce_cart_item_removed_because_modified_message
**Params:** string $message, WC_Product $product
**Since:** 3.8.0 | **Tags:** #filter
Filter message about item removed from the cart because it has since been modified.

### woocommerce_cart_item_removed_message
**Params:** string $message, WC_Product $product
**Since:** 3.8.0 | **Tags:** #filter
Filter message about item removed from the cart.

### woocommerce_cart_item_removed_notice_type
**Args:** 'success'
**Tags:** #filter

### woocommerce_cart_item_removed_title
**Params:** string $cart_item_key, \WC_Cart $cart
**Since:** 10.6.0 | **Tags:** #filter
Fires when a cart item is removed from a user request.

### woocommerce_cart_item_required_stock_is_not_enough
**Params:** bool $has_stock, WC_Product $product, array $values
**Since:** 4.6.0 | **Tags:** #filter
Allows filter if product have enough stock to get added to the cart.

### woocommerce_cart_needs_payment
**Args:** 0 < $this->get_total( 'edit' ), $this
**Tags:** #filter

### woocommerce_cart_needs_shipping
**Args:** $needs_shipping
**Tags:** #filter

### woocommerce_cart_product_cannot_add_another_message
**Params:** string $message, WC_Product $product_data
**Since:** 4.5.0 | **Tags:** #filter
Filters message about more than 1 product being added to cart.

### woocommerce_cart_product_cannot_be_purchased_message
**Params:** string $message, WC_Product $product_data
**Since:** 3.8.0 | **Tags:** #filter
Filters message about product unable to be purchased.

### woocommerce_cart_product_not_enough_stock_already_in_cart_message
**Params:** string $message, WC_Product $product_data, int $stock_quantity, int $stock_quantity_in_cart
**Since:** 5.3.0 | **Tags:** #filter
Filters message about product not having enough stock accounting for what's already in the cart.

### woocommerce_cart_product_not_enough_stock_message
**Params:** string $message, WC_Product $product_data, int $stock_quantity
**Since:** 4.5.0 | **Tags:** #filter
Filters message about product not having enough stock.

### woocommerce_cart_product_out_of_stock_message
**Params:** string $message, WC_Product $product_data
**Since:** 4.5.0 | **Tags:** #filter
Filters message about product being out of stock.

### woocommerce_cart_product_price
**Args:** wc_price( $product_price ), $product
**Tags:** #filter

### woocommerce_cart_product_subtotal
**Args:** $product_subtotal, $product, $quantity, $this
**Tags:** #filter

### woocommerce_cart_ready_to_calc_shipping
**Params:** bool $ready
**Since:** 2.7.0 | **Tags:** #filter
Filter to allow plugins to prevent shipping calculations.

### woocommerce_cart_redirect_after_error
**Args:** get_permalink( $product_id ), $product_id
**Tags:** #filter

### woocommerce_cart_remove_taxes_zero_rate_id
**Params:** string $tax_rate_id
**Since:** 3.0.0 | **Tags:** #filter
Controls the zero rate tax ID. An order item tax will not be created for this ID (which by default is 'zero-rated').

### woocommerce_cart_session_initialize
**Params:** bool $must_initialize, bool $session
**Since:** 6.9.0 | **Tags:** #filter
Filters whether hooks should be initialized for the current cart session.

### woocommerce_cart_shipping_packages
**Params:** array $packages
**Since:** 1.5.4 | **Tags:** #filter
Filters the shipping packages for the cart.

### woocommerce_cart_shipping_total
**Args:** $total, $this
**Tags:** #filter

### woocommerce_cart_subtotal
**Args:** $cart_subtotal, $compound, $this
**Tags:** #filter

### woocommerce_cart_tax_totals
**Args:** $tax_totals, $this
**Tags:** #filter

### woocommerce_cart_taxes_total
**Args:** $total, $compound, $display, $this
**Tags:** #filter

### woocommerce_cart_total
**Args:** wc_price( $total )
**Tags:** #filter

### woocommerce_cart_total_discount
**Args:** $this->get_discount_total() ? wc_price( $this->get_discount_total() ) : false, $this
**Tags:** #filter

### woocommerce_cart_total_ex_tax
**Args:** wc_price( max( 0, $this->get_total( 'edit' ) - $this->get_total_tax() ) )
**Tags:** #filter

### woocommerce_cart_totals_coupon_html
**Args:** $coupon_html, $coupon, $discount_amount_html
**Tags:** #filter

### woocommerce_cart_totals_coupon_label
**Params:** string|WC_Coupon $coupon, bool $echo
**Tags:** #filter
Get a coupon label.

### woocommerce_cart_totals_fee_html
**Args:** $cart_totals_fee_html, $fee
**Tags:** #filter

### woocommerce_cart_totals_get_fees_from_cart_taxes
**Args:** $fee->taxes, $fee, $this
**Tags:** #filter

### woocommerce_cart_totals_get_item_tax_rates
**Args:** $item_tax_rates, $item, $this->cart
**Tags:** #filter

### woocommerce_cart_totals_order_total_html
**Args:** $value
**Tags:** #filter

### woocommerce_cart_totals_taxes_total_html
**Args:** wc_price( WC()->cart->get_taxes_total() )
**Tags:** #filter

### woocommerce_cart_updated_notice_type
**Args:** 'success'
**Tags:** #filter

### woocommerce_get_cart_contents
**Args:** (array) $this->cart_contents
**Tags:** #filter

### woocommerce_get_cart_item_from_session
**Params:** array $session_data, array $values, string $key
**Since:** 3.2.0 | **Tags:** #filter
Filter to modify or add session data to the cart contents.

### woocommerce_get_cart_tax
**Args:** $cart_total_tax ? wc_price( $cart_total_tax ) : ''
**Tags:** #filter

### woocommerce_get_cart_url
**Params:** string $cart_url
**Since:** 2.5.0 | **Tags:** #filter
Filter the cart URL.

### woocommerce_is_cart
**Params:** bool $is_cart
**Since:** 2.4.0 | **Tags:** #filter
Filter to allow for custom logic to determine if the cart page is being viewed.

### woocommerce_persistent_cart_enabled
**Params:** bool $enabled
**Since:** 3.4.0 | **Tags:** #filter
Filters whether the persistent cart is enabled.

### woocommerce_pre_remove_cart_item_from_session
**Params:** bool $remove_cart_item_from_session, string $key, array $values, WC_Product $product
**Since:** 3.6.0 | **Tags:** #filter
Allow 3rd parties to validate this item before it's added to cart and add their own notices.

### woocommerce_should_clear_cart_after_payment
**Params:** bool $should_clear_cart_after_payment
**Since:** 9.3.0 | **Tags:** #filter
Determine whether the cart should be cleared after payment.

### woocommerce_stock_amount_cart_item
**Args:** wc_stock_amount( preg_replace( '/[^0-9\.]/', '', $cart_totals[ $cart_item_key ]['qty'] ) ), $cart_item_key
**Tags:** #filter

### woocommerce_store_api_add_to_cart_data
**Params:** array $add_to_cart_data
**Since:** 8.8.0 | **Tags:** #filter
Filters cart item data sent via the API before it is passed to the cart controller. This hook filters cart items. It allows the request data to be changed, for example, quantity, or supplemental cart item data, before it is passed into CartController::add_to_cart and stored to session. CartController::add_to_cart only expects the keys id, quantity, variation, and cart_item_data, so other values may be ignored. CartController::add_to_cart (and core) do already have a filter hook called woocommerce_add_cart_item, but this does not have access to the original Store API request like this hook does.

### woocommerce_store_api_cart_item_images
**Params:** array $product_images, array $cart_item, string $cart_item_key
**Since:** 9.6.0 | **Tags:** #filter
Filter the cart product images. This hook allows the cart item images to be changed. This is specific to the cart endpoint.

### woocommerce_update_cart_action_cart_updated
**Args:** $cart_updated
**Tags:** #filter

### woocommerce_update_cart_validation
**Args:** true, $cart_item_key, $values, $quantity
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
