# WooCommerce Filters: Shipping

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_cart_no_shipping_available_html
**Params:** string $html, string $formatted_destination
**Since:** 3.0.0 | **Tags:** #filter
Provides a means of overriding the default 'no shipping available' HTML string.

### woocommerce_no_shipping_available_html
**Args:** __( 'There are no shipping options available. Please ensure that your address has been entered correctly, or contact us if you need any help.', 'woocommerce' )
**Tags:** #filter

### woocommerce_shipping_calculator_enable_city
**Args:** true
**Tags:** #filter

### woocommerce_shipping_calculator_enable_country
**Args:** true
**Tags:** #filter

### woocommerce_shipping_calculator_enable_postcode
**Params:** bool $show_postcode
**Since:** 8.4.0 | **Tags:** #filter
Filter to not require shipping postcode for shipping calculation, even if it is required at checkout. This can be used to allow shipping calculations to be done without a postcode.

### woocommerce_shipping_calculator_enable_state
**Params:** bool $show_state
**Since:** 8.4.0 | **Tags:** #filter
Filter to not require shipping state for shipping calculation, even if it is required at checkout. This can be used to allow shipping calculations to be done without a state.

### woocommerce_shipping_estimate_html
**Args:** __( 'Shipping options will be updated during checkout.', 'woocommerce' )
**Tags:** #filter

### woocommerce_shipping_may_be_available_html
**Args:** __( 'Enter your address to view shipping options.', 'woocommerce' )
**Tags:** #filter

### woocommerce_shipping_not_enabled_on_cart_html
**Args:** __( 'Shipping costs are calculated during checkout.', 'woocommerce' )
**Tags:** #filter

### woocommerce_shortcode_order_tracking_order_id
**Args:** $order_id
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXshipping_class_id
**Tags:** #filter

### wc_shipping_enabled
**Args:** get_option( 'woocommerce_ship_to_countries' ) !== 'disabled'
**Tags:** #filter

### woocommerce_allow_shipping_partner_suggestions
**Args:** true
**Tags:** #filter

### woocommerce_apply_tracking
**Args:** true
**Tags:** #filter

### woocommerce_apply_user_tracking
**Args:** true
**Tags:** #filter

### woocommerce_calc_shipping_tax
**Args:** $taxes, $price, $rates
**Tags:** #filter

### woocommerce_cart_needs_shipping_address
**Args:** true === $this->needs_shipping() && ! wc_ship_to_billing_address_only()
**Tags:** #filter

### woocommerce_cart_shipping_method_full_label
**Args:** $label, $method
**Tags:** #filter

### woocommerce_countries_shipping_countries
**Params:** array $countries
**Since:** 3.3.0 | **Tags:** #filter
Filter the list of allowed selling countries.

### woocommerce_countries_shipping_country_states
**Args:** $states
**Tags:** #filter

### woocommerce_countries_shipping_to_prefix
**Args:** $return, $country_code
**Tags:** #filter

### woocommerce_evaluate_shipping_cost_args
**Args:** $args, $sum, $this
**Tags:** #filter

### woocommerce_fulfillment_parse_tracking_number
**Args:** $tracking_number, WC()->countries->get_base_country(), $order->get_shipping_country()
**Tags:** #filter

### woocommerce_fulfillment_shipping_providers
**Params:** array $shipping_providers
**Since:** 10.1.0 | **Tags:** #filter
This filter allows plugins to modify the list of shipping providers. It can be used to add, remove, or change the shipping providers available in the WooCommerce Fulfillments system.

### woocommerce_ga_disable_tracking
**Params:** boolean $disable_tracking
**Since:** 4.9.0 | **Tags:** #filter
Filter to disable Google Analytics tracking.

### woocommerce_get_shipping_classes
**Args:** $this->shipping_classes
**Tags:** #filter

### woocommerce_get_shipping_tax
**Params:** array $taxes, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate taxes.

### woocommerce_max_webhook_delivery_failures
**Args:** 5
**Tags:** #filter

### woocommerce_order_shipping_method
**Args:** implode( ', ', $names ), $this
**Tags:** #filter

### woocommerce_package_rates
**Args:** $package['rates'], $package
**Tags:** #filter

### woocommerce_partial_download_tracking_window
**Params:** int $window_in_seconds, int $download_permission_id
**Since:** 9.2.0 | **Tags:** #filter
Determines how long the window of time is for tracking unique download attempts, in relation to partial (ranged) download requests.

### woocommerce_shipping_$METHOD->ID_instance_settings_values
**Tags:** #filter

### woocommerce_shipping_$THIS->ID_instance_option
**Tags:** #filter

### woocommerce_shipping_$THIS->ID_instance_settings_values
**Tags:** #filter

### woocommerce_shipping_$THIS->ID_is_available
**Tags:** #filter

### woocommerce_shipping_$THIS->ID_option
**Tags:** #filter

### woocommerce_shipping_address_map_url
**Args:** 'https://maps.google.com/maps?&q=' . rawurlencode( implode( ', ', $address ) ) . '&z=16', $this
**Tags:** #filter

### woocommerce_shipping_address_map_url_parts
**Args:** $address, $this
**Tags:** #filter

### woocommerce_shipping_chosen_method
**Params:** string $default, array $rates, string $chosen_method
**Since:** 3.2.0 | **Tags:** #filter
Filters the default shipping method for a package.

### woocommerce_shipping_classes_columns
**Args:** array(
				'wc-shipping-class-name'        => __( 'Shipping class', 'woocommerce' ),
				'wc-shipping-class-slug'        => __( 'Slug', 'woocommerce' ),
				'wc-shipping-class-description' => __( 'Description', 'woocommerce' ),
				'wc-shipping-class-count'       => __( 'Product count', 'woocommerce' ),
			)
**Tags:** #filter

### woocommerce_shipping_instance_form_fields_$THIS->ID
**Tags:** #filter

### woocommerce_shipping_method_add_rate
**Args:** $rate, $args, $this
**Tags:** #filter

### woocommerce_shipping_method_add_rate_args
**Params:** array $args
**Tags:** #filter
Add a shipping rate. If taxes are not set they will be calculated based on cost.

### woocommerce_shipping_method_description
**Args:** $this->method_description, $this
**Tags:** #filter

### woocommerce_shipping_method_supports
**Params:** string $feature
**Tags:** #filter
Check if a shipping method supports a given feature. Methods should override this to declare support (or lack of support) for a feature.

### woocommerce_shipping_method_title
**Args:** $this->method_title, $this
**Tags:** #filter

### woocommerce_shipping_methods
**Args:** $shipping_methods
**Tags:** #filter

### woocommerce_shipping_package_details_array
**Args:** $product_names, $package
**Tags:** #filter

### woocommerce_shipping_package_name
**Params:** string $shipping_package_name, string $package_id, array $package, int $total_packages
**Since:** 4.3.0 | **Tags:** #filter
Filters the shipping package name.

### woocommerce_shipping_packages
**Params:** array $packages
**Since:** 2.6.0 | **Tags:** #filter
Allow packages to be reorganized after calculating the shipping. This filter can be used to apply some extra manipulation after the shipping costs are calculated for the packages but before WooCommerce does anything with them. A good example of usage is to merge the shipping methods for multiple packages for marketplaces.

### woocommerce_shipping_prices_include_tax
**Params:** bool $shipping_prices_include_tax
**Since:** 10.6.0 | **Tags:** #filter
Filter whether shipping prices include tax.

### woocommerce_shipping_rate_cost
**Params:** string $cost, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate cost.

### woocommerce_shipping_rate_delivery_time
**Params:** string $delivery_time, WC_Shipping_Rate $this
**Since:** 9.2.0 | **Tags:** #filter
Filter the shipping rate delivery time.

### woocommerce_shipping_rate_description
**Params:** string $description, WC_Shipping_Rate $this
**Since:** 9.2.0 | **Tags:** #filter
Filter the shipping rate description.

### woocommerce_shipping_rate_id
**Params:** string $id, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate ID.

### woocommerce_shipping_rate_instance_id
**Params:** int $instance_id, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate instance ID.

### woocommerce_shipping_rate_label
**Params:** string $label, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate label.

### woocommerce_shipping_rate_method_id
**Params:** string $method_id, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping method ID.

### woocommerce_shipping_rate_tax_status
**Params:** string $tax_status, WC_Shipping_Rate $this
**Since:** 9.9.0 | **Tags:** #filter
Filter to allow tax status to be overridden for a shipping rate.

### woocommerce_shipping_rate_taxes
**Params:** array $taxes, WC_Shipping_Rate $this
**Since:** 3.2.0 | **Tags:** #filter
Filter the shipping rate taxes.

### woocommerce_shipping_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_shipping_show_shipping_calculator
**Args:** $first, $i, $package
**Tags:** #filter

### woocommerce_shipping_tax_class
**Params:** string|null $tax_class, WC_Cart|null $cart, WC_Customer|null $customer, array $location
**Since:** 10.5.0 | **Tags:** #filter
Filters the shipping tax class before calculating tax rates. This filter allows plugins to modify or replace the shipping tax class that will be used to calculate shipping tax rates. It fires after core logic determines the tax class but before rates are looked up.

### woocommerce_shipping_zone_shipping_methods
**Args:** $methods, $raw_methods, $allowed_classes, $this
**Tags:** #filter

### woocommerce_taxonomy_args_product_shipping_class
**Args:** array(
					'hierarchical'          => false,
					'update_count_callback' => '_update_post_term_count',
					'label'                 => __( 'Shipping classes', 'woocommerce' ),
					'labels'                => array(
						'name'              => __( 'Product shipping classes', 'woocommerce' ),
						'singular_name'     => __( 'Shipping class', 'woocommerce' ),
						'menu_name'         => _x( 'Shipping classes', 'Admin menu name', 'woocommerce' ),
						'search_items'      => __( 'Search shipping classes', 'woocommerce' ),
						'all_items'         => __( 'All shipping classes', 'woocommerce' ),
						'parent_item'       => __( 'Parent shipping class', 'woocommerce' ),
						'parent_item_colon' => __( 'Parent shipping class:', 'woocommerce' ),
						'edit_item'         => __( 'Edit shipping class', 'woocommerce' ),
						'update_item'       => __( 'Update shipping class', 'woocommerce' ),
						'add_new_item'      => __( 'Add new shipping class', 'woocommerce' ),
						'new_item_name'     => __( 'New shipping class Name', 'woocommerce' ),
					),
					'public'                => false,
					'show_ui'               => false,
					'show_in_quick_edit'    => false,
					'show_in_nav_menus'     => false,
					'query_var'             => is_admin(),
					'capabilities'          => array(
						'manage_terms' => 'manage_product_terms',
						'edit_terms'   => 'edit_product_terms',
						'delete_terms' => 'delete_product_terms',
						'assign_terms' => 'assign_product_terms',
					),
					'rewrite'               => false,
				)
**Tags:** #filter

### woocommerce_taxonomy_objects_product_shipping_class
**Args:** array( 'product', 'product_variation' )
**Tags:** #filter

### woocommerce_webhook_delivery_url
**Args:** $this->get_prop( 'delivery_url', $context ), $this->get_id()
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
