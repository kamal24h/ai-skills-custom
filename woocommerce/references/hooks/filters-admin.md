# WooCommerce Filters: Admin

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_attribute
**Args:** wpautop( wptexturize( implode( ', ', $values ) ) ), $attribute, $values
**Tags:** #filter

### woocommerce_page_title
**Args:** $page_title
**Tags:** #filter

### woocommerce_taxonomy_archive_description_raw
**Params:** string $term_description, WP_Term $term
**Since:** 6.7.0 | **Tags:** #filter
Filters the archive's raw description on taxonomy archives.

### experimental_woocommerce_admin_payment_reactify_render_sections
**Params:** array $sections
**Since:** 9.3.0 | **Tags:** #filter
Modify the optional set of payments settings sections to be rendered using React. This filter allows plugins to add or remove optional sections (typically offline gateways) that should be rendered using React. Sections should be identified by their gateway IDs. Note: The main Payments page ("main") and the Offline overview ("offline") are always React-only and cannot be disabled via this filter.

### wc_admin_reports_path
**Args:** 'reports/class-wc-report-' . $name . '.php', $name, $class
**Tags:** #filter

### wc_admin_show_legacy_coupon_menu
**Params:** bool $display
**Since:** 10.5.0 | **Tags:** #filter
Filter to determine whether to display the legacy coupon menu item.

### wc_currency_settings
**Args:** array(
				'code'              => $code,
				'precision'         => wc_get_price_decimals(),
				'symbol'            => html_entity_decode( get_woocommerce_currency_symbol( $code ) ),
				'symbolPosition'    => get_option( 'woocommerce_currency_pos' ),
				'decimalSeparator'  => wc_get_price_decimal_separator(),
				'thousandSeparator' => wc_get_price_thousand_separator(),
				'priceFormat'       => html_entity_decode( get_woocommerce_price_format() ),
			)
**Tags:** #filter

### woocommerce_$THIS->ID_settings
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_columns
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_css_classes
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_default_statuses
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_disable_months_filter
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_order_count
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_order_css_classes
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_prepare_items_query_args
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_request
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_should_render_blank_state
**Tags:** #filter

### woocommerce_$THIS->ORDER_TYPE_list_table_sortable_columns
**Tags:** #filter

### woocommerce_admin_allowed_promo_notes
**Params:** array $promo_notes
**Since:** 7.8.0 | **Tags:** #filter
Filter allowed promo notes for experimental-activate-promo.

### woocommerce_admin_billing_fields
**Params:** WC_Order|false $order, string $context
**Since:** 1.4.0 | **Tags:** #filter
Provides an opportunity to modify the list of order billing fields displayed on the admin.

### woocommerce_admin_dashboard_recent_reviews
**Params:** string $product_title, \stdClass $comment
**Since:** 2.1.0 | **Tags:** #filter
Filters the product name for display in the latest reviews.

### woocommerce_admin_disabled
**Params:** bool $disabled
**Tags:** #filter
Filter allowing WooCommerce Admin optional features to be disabled.

### woocommerce_admin_download_permissions_title
**Args:** $product->get_name(), $download->get_product_id(), $download->get_order_id(), $download->get_order_key(), $download->get_download_id()
**Tags:** #filter

### woocommerce_admin_downloads_report_downloads_per_page
**Args:** 20
**Tags:** #filter

### woocommerce_admin_experimental_onboarding_tasklists
**Params:** array $lists
**Since:** 7.4 | **Tags:** #filter
Filter to override default task lists.

### woocommerce_admin_export_id
**Args:** $default_export_id
**Tags:** #filter

### woocommerce_admin_features
**Args:** array()
**Tags:** #filter

### woocommerce_admin_get_feature_config
**Args:** wc_admin_get_feature_config()
**Tags:** #filter

### woocommerce_admin_get_user_data_fields
**Params:** array $fields
**Since:** 4.0.0 | **Tags:** #filter
Filter user data fields exposed over the WordPress user endpoint.

### woocommerce_admin_html_order_item_class
**Args:** ! empty( $class ) ? $class : '', $item, $order
**Tags:** #filter

### woocommerce_admin_html_order_preview_item_class
**Args:** '', $item, $order
**Tags:** #filter

### woocommerce_admin_is_loading
**Params:** bool $is_loading
**Since:** 6.5.0 | **Tags:** #filter
Some routes or features like onboarding hide the wp-admin navigation and masterbar. Setting `woocommerce_admin_is_loading` to true allows us to premeptively hide these elements while the JS app loads. This class needs to be removed by those feature components (like <ProfileWizard />).

### woocommerce_admin_meta_boxes_prepare_attribute
**Params:** array $data
**Tags:** #filter
Prepare attributes for save.

### woocommerce_admin_meta_boxes_variations_count
**Args:** $wpdb->get_var( $wpdb->prepare( "SELECT COUNT(ID) FROM $wpdb->posts WHERE post_parent = %d AND post_type = 'product_variation' AND post_status IN ('publish', 'private')", $post->ID ) ), $post->ID
**Tags:** #filter

### woocommerce_admin_meta_boxes_variations_per_page
**Args:** 15
**Tags:** #filter

### woocommerce_admin_obsolete_notes_names
**Args:** array()
**Tags:** #filter

### woocommerce_admin_onboarding_homepage_template
**Params:** string $template
**Tags:** #filter
Modify the template/content of the default homepage.

### woocommerce_admin_onboarding_industries
**Params:** array $industries
**Since:** 6.5.0 | **Tags:** #filter
Filter the list of industries.

### woocommerce_admin_onboarding_industry_image
**Args:** WC_ADMIN_IMAGES_FOLDER_URL . '/onboarding/other-small.jpg', $industry_slug
**Tags:** #filter

### woocommerce_admin_onboarding_jetpack_connect_redirect_url
**Args:** esc_url_raw( $request['redirect_url'] )
**Tags:** #filter

### woocommerce_admin_onboarding_preloaded_data
**Args:** $settings
**Tags:** #filter

### woocommerce_admin_onboarding_product_types
**Args:** $products
**Tags:** #filter

### woocommerce_admin_onboarding_tasks
**Args:** $json
**Tags:** #filter

### woocommerce_admin_order_actions
**Params:** array $action, WC_Order $order
**Since:** 6.7.0 | **Tags:** #filter
Provides an opportunity to modify the action buttons within the order list table.

### woocommerce_admin_order_buyer_name
**Params:** string $buyer, WC_Order $order
**Since:** 3.7.0 | **Tags:** #filter
Filter buyer name in list table orders.

### woocommerce_admin_order_date_format
**Args:** __( 'M j, Y', 'woocommerce' )
**Tags:** #filter

### woocommerce_admin_order_item_coupon_url
**Args:** add_query_arg(
									array(
										'post'   => $post_id,
										'action' => 'edit',
									),
									admin_url( 'post.php' )
								), $item, $order
**Tags:** #filter

### woocommerce_admin_order_item_thumbnail
**Args:** $product->get_image( 'thumbnail', array( 'title' => '' ), false ), $item_id, $item
**Tags:** #filter

### woocommerce_admin_order_item_types
**Args:** 'line_item'
**Tags:** #filter

### woocommerce_admin_order_milestone_statuses
**Params:** array $allowed_statuses
**Since:** 3.5.0 | **Tags:** #filter
Filter Order statuses that will count towards milestones.

### woocommerce_admin_order_milestones_enabled
**Args:** true
**Tags:** #filter

### woocommerce_admin_order_preview_actions
**Args:** $actions, $order
**Tags:** #filter

### woocommerce_admin_order_preview_get_order_details
**Params:** array $order_details
**Tags:** #filter
Filter to customize the order details data that the woocommerce_get_order_details action will send.

### woocommerce_admin_order_preview_line_item_column_sanitize_key$COLUMN
**Tags:** #filter

### woocommerce_admin_order_preview_line_item_columns
**Args:** array(
				'product'  => __( 'Product', 'woocommerce' ),
				'quantity' => __( 'Quantity', 'woocommerce' ),
				'tax'      => __( 'Tax', 'woocommerce' ),
				'total'    => __( 'Total', 'woocommerce' ),
			), $order
**Tags:** #filter

### woocommerce_admin_order_preview_line_items
**Args:** $order->get_items(), $order
**Tags:** #filter

### woocommerce_admin_order_should_render_refunds
**Params:** bool $render_refunds, int $order_id, WC_Order $order
**Since:** 6.4.0 | **Tags:** #filter
Allow plugins to determine whether refunds UI should be rendered in the template.

### woocommerce_admin_payment_gateway_suggestion_specs
**Args:** $specs
**Tags:** #filter

### woocommerce_admin_plugins_pre_activate
**Params:** array $plugins
**Since:** 6.4.0 | **Tags:** #filter
Filter the list of plugins to activate.

### woocommerce_admin_plugins_pre_install
**Params:** array $plugins
**Since:** 6.4.0 | **Tags:** #filter
Filter the list of plugins to install.

### woocommerce_admin_preload_options
**Args:** array()
**Tags:** #filter

### woocommerce_admin_preload_settings
**Args:** array()
**Tags:** #filter

### woocommerce_admin_product_term_list
**Args:** implode( ', ', $termlist ), 'product_cat', $this->object->get_id(), $termlist, $terms
**Tags:** #filter

### woocommerce_admin_remote_specs_evaluator_should_log
**Params:** bool $should_log
**Since:** 9.2.0 | **Tags:** #filter
Filter to determine if the rule evaluator should log the results.

### woocommerce_admin_report_chart_data
**Args:** $data
**Tags:** #filter

### woocommerce_admin_report_columns
**Args:** $this->report_columns, $this->context, self::get_db_table_name()
**Tags:** #filter

### woocommerce_admin_report_customer_list_user_query_args
**Args:** array(
					'exclude' => $privileged_users->get_results(),
					'number'  => $per_page,
					'offset'  => ( $current_page - 1 ) * $per_page,
				)
**Tags:** #filter

### woocommerce_admin_report_customers_user_query_args
**Args:** array(
					'fields'  => array( 'user_registered' ),
					'exclude' => $privileged_users->get_results(),
				)
**Tags:** #filter

### woocommerce_admin_report_data
**Args:** $this->report_data
**Tags:** #filter

### woocommerce_admin_reports
**Params:** array $reports
**Tags:** #filter
Filter the list and add reports to the legacy _WooCommerce > Reports_. Array items should be in the format of $reports['automatewoo'] = array( 'title'   => 'AutomateWoo', 'reports' => array( 'runs_by_date' => array( 'title'       => __( 'Workflow Runs', 'automatewoo' ), 'description' => '', 'hide_title'  => false, 'callback'    => array( $this, 'get_runs_by_date' ), ), // ... ), ); This filter has a colliding name with the one in Automattic\WooCommerce\Admin\API\Reports\Controller. To make sure your code runs in the context of the legacy _WooCommerce > Reports_ screen, and not the REST endpoint, use the following: add_filter( 'woocommerce_admin_reports', function( $reports ) { if ( is_admin() ) { // ...

### woocommerce_admin_sales_record_milestone_enabled
**Args:** true
**Tags:** #filter

### woocommerce_admin_settings_sanitize_option
**Args:** $value, $option, $raw_value
**Tags:** #filter

### woocommerce_admin_settings_sanitize_option_$OPTION_NAME
**Tags:** #filter

### woocommerce_admin_shared_settings
**Args:** array()
**Since:** 6.4.0 | **Tags:** #filter
Filters the shared settings that are passed to the client.

### woocommerce_admin_shipping_fields
**Params:** WC_Order|false $order, string $context
**Since:** 1.4.0 | **Tags:** #filter
Provides an opportunity to modify the list of order shipping fields displayed on the admin.

### woocommerce_admin_shipping_partner_suggestions_specs
**Args:** DefaultShippingPartners::get_all()
**Tags:** #filter

### woocommerce_admin_should_load_features
**Params:** boolean $should_load
**Since:** 9.6.0 | **Tags:** #filter
Filter to determine if admin features should be loaded.

### woocommerce_admin_status_tabs
**Args:** $tabs
**Tags:** #filter

### woocommerce_admin_stock_html
**Args:** $stock_html, $this->object
**Tags:** #filter

### woocommerce_admin_stock_report_product_actions
**Args:** $actions, $product
**Tags:** #filter

### woocommerce_admin_stock_report_products_per_page
**Args:** 20
**Tags:** #filter

### woocommerce_admin_survey_query
**Args:** $query
**Tags:** #filter

### woocommerce_admin_terms_metabox_datalimit
**Params:** int $term_limit
**Since:** 8.8.0 | **Tags:** #filter
Filter the length (number of terms) rendered in the list.

### woocommerce_admin_third_party_tax_setup_complete
**Args:** false
**Tags:** #filter

### woocommerce_admin_user_actions
**Args:** $actions, $user
**Tags:** #filter

### woocommerce_admin_woopayments_onboarding_task_additional_data
**Params:** ?array $additional_data
**Since:** 9.4.0 | **Tags:** #filter
Filter WooPayments onboarding task additional data.

### woocommerce_admin_woopayments_onboarding_task_badge
**Params:** string $badge
**Since:** 8.2.0 | **Tags:** #filter
Filter WooPayments onboarding task badge.

### woocommerce_after_dashboard_status_widget_parameter
**Args:** null
**Tags:** #filter

### woocommerce_attribute_default_is_variation
**Args:** ProductType::VARIABLE === $product_type ? 1 : 0, $product_type
**Tags:** #filter

### woocommerce_attribute_default_visibility
**Args:** 1
**Tags:** #filter

### woocommerce_attribute_label
**Args:** $label, $name, $product
**Tags:** #filter

### woocommerce_attribute_lookup_regeneration_step_size
**Params:** int $count
**Since:** 6.3 | **Tags:** #filter
Filter to alter the count of products that will be processed in each step of the product attributes lookup table regeneration process.

### woocommerce_attribute_orderby
**Args:** isset( $taxonomies[ 'id:' . $id ] ) ? $taxonomies[ 'id:' . $id ]->attribute_orderby : 'menu_order', $name
**Tags:** #filter

### woocommerce_attribute_show_in_nav_menus
**Args:** false, $name
**Tags:** #filter

### woocommerce_attribute_taxonomies
**Params:** array $attribute_taxonomies
**Tags:** #filter
Filter attribute taxonomies.

### woocommerce_brands_settings_fields
**Params:** array $settings
**Since:** 9.4.0 | **Tags:** #filter
Filter Brands settings.

### woocommerce_com_integration_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_component_settings_preload_endpoints
**Args:** array()
**Tags:** #filter

### woocommerce_dashboard_status_widget_reports
**Args:** $status_widget_reports
**Tags:** #filter

### woocommerce_dashboard_status_widget_top_seller_query
**Params:** array $query
**Since:** 2.2.0 | **Tags:** #filter
Allows modification of the query to determine the top seller product in the dashboard status widget.

### woocommerce_disable_admin_bar
**Params:** bool $enabled
**Since:** 3.0.0 | **Tags:** #filter
Controls whether the WooCommerce admin bar should be disabled.

### woocommerce_dismiss_admin_notice_capability
**Params:** string $default_capability, string $notice_name
**Since:** 6.7.0 | **Tags:** #filter
Filter the capability required to dismiss a given notice.

### woocommerce_display_admin_footer_text
**Args:** in_array( $current_screen->id, $wc_pages, true )
**Tags:** #filter

### woocommerce_enable_admin_help_tab
**Args:** true
**Tags:** #filter

### woocommerce_gateway_$GATEWAY->ID_settings_values
**Tags:** #filter

### woocommerce_general_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_get_settings_$THIS->ID
**Tags:** #filter

### woocommerce_get_settings_pages
**Args:** $settings
**Tags:** #filter

### woocommerce_helper_suppress_admin_notices
**Args:** false
**Tags:** #filter

### woocommerce_hpos_admin_search_filters
**Args:** $options
**Since:** 8.9.0. | **Tags:** #filter
Filters the search filters available in the admin order search. Can be used to add new or remove existing filters. When adding new filters, `woocommerce_hpos_generate_where_for_search_filter` should also be used to generate the WHERE clause for the new filter

### woocommerce_payment_gateway_enabled_notification_settings_url
**Params:** string $gateway_settings_url, WC_Payment_Gateway $gateway
**Since:** 10.7.0 | **Tags:** #filter
Filters the payment gateway settings URL for the admin payment gateway enabled email.

### woocommerce_prevent_admin_access
**Args:** $prevent_access
**Tags:** #filter

### woocommerce_products_admin_list_table_filters
**Args:** array(
				'product_category' => array( $this, 'render_products_category_filter' ),
				'product_type'     => array( $this, 'render_products_type_filter' ),
				'stock_status'     => array( $this, 'render_products_stock_status_filter' ),
			)
**Tags:** #filter

### woocommerce_register_post_type_product
**Args:** array(
					'labels'              => array(
						'name'                  => __( 'Products', 'woocommerce' ),
						'singular_name'         => __( 'Product', 'woocommerce' ),
						'all_items'             => __( 'All Products', 'woocommerce' ),
						'menu_name'             => _x( 'Products', 'Admin menu name', 'woocommerce' ),
						'add_new'               => __( 'Add New', 'woocommerce' ),
						'add_new_item'          => __( 'Add new product', 'woocommerce' ),
						'edit'                  => __( 'Edit', 'woocommerce' ),
						'edit_item'             => __( 'Edit product', 'woocommerce' ),
						'new_item'              => __( 'New product', 'woocommerce' ),
						'view_item'             => __( 'View product', 'woocommerce' ),
						'view_items'            => __( 'View products', 'woocommerce' ),
						'search_items'          => __( 'Search products', 'woocommerce' ),
						'not_found'             => __( 'No products found', 'woocommerce' ),
						'not_found_in_trash'    => __( 'No products found in trash', 'woocommerce' ),
						'parent'                => __( 'Parent product', 'woocommerce' ),
						'featured_image'        => __( 'Product image', 'woocommerce' ),
						'set_featured_image'    => __( 'Set product image', 'woocommerce' ),
						'remove_featured_image' => __( 'Remove product image', 'woocommerce' ),
						'use_featured_image'    => __( 'Use as product image', 'woocommerce' ),
						'insert_into_item'      => __( 'Insert into product', 'woocommerce' ),
						'uploaded_to_this_item' => __( 'Uploaded to this product', 'woocommerce' ),
						'filter_items_list'     => __( 'Filter products', 'woocommerce' ),
						'items_list_navigation' => __( 'Products navigation', 'woocommerce' ),
						'items_list'            => __( 'Products list', 'woocommerce' ),
						'item_link'             => __( 'Product Link', 'woocommerce' ),
						'item_link_description' => __( 'A link to a product.', 'woocommerce' ),
					),
					'description'         => __( 'This is where you can browse products in this store.', 'woocommerce' ),
					'public'              => true,
					'show_ui'             => true,
					'menu_icon'           => 'dashicons-archive',
					'capability_type'     => 'product',
					'map_meta_cap'        => true,
					'publicly_queryable'  => true,
					'exclude_from_search' => false,
					'hierarchical'        => false, // Hierarchical causes memory issues - WP loads all records!
					'rewrite'             => $permalinks['product_rewrite_slug'] ? array(
						'slug'       => $permalinks['product_rewrite_slug'],
						'with_front' => false,
						'feeds'      => true,
					) : false,
					'query_var'           => true,
					'supports'            => $supports,
					'has_archive'         => $has_archive,
					'show_in_nav_menus'   => true,
					'show_in_rest'        => true,
				)
**Tags:** #filter

### woocommerce_register_post_type_product_form
**Tags:** #filter

### woocommerce_register_post_type_product_variation
**Args:** array(
					'label'           => __( 'Variations', 'woocommerce' ),
					'public'          => false,
					'hierarchical'    => false,
					'supports'        => false,
					'capability_type' => 'product',
					'rewrite'         => false,
				)
**Tags:** #filter

### woocommerce_register_post_type_shop_coupon
**Args:** array(
						'labels'              => array(
							'name'                  => __( 'Coupons', 'woocommerce' ),
							'singular_name'         => __( 'Coupon', 'woocommerce' ),
							'menu_name'             => _x( 'Coupons', 'Admin menu name', 'woocommerce' ),
							'add_new'               => __( 'Add coupon', 'woocommerce' ),
							'add_new_item'          => __( 'Add new coupon', 'woocommerce' ),
							'edit'                  => __( 'Edit', 'woocommerce' ),
							'edit_item'             => __( 'Edit coupon', 'woocommerce' ),
							'new_item'              => __( 'New coupon', 'woocommerce' ),
							'view_item'             => __( 'View coupon', 'woocommerce' ),
							'search_items'          => __( 'Search coupons', 'woocommerce' ),
							'not_found'             => __( 'No coupons found', 'woocommerce' ),
							'not_found_in_trash'    => __( 'No coupons found in trash', 'woocommerce' ),
							'parent'                => __( 'Parent coupon', 'woocommerce' ),
							'filter_items_list'     => __( 'Filter coupons', 'woocommerce' ),
							'items_list_navigation' => __( 'Coupons navigation', 'woocommerce' ),
							'items_list'            => __( 'Coupons list', 'woocommerce' ),
						),
						'description'         => __( 'This is where you can add new coupons that customers can use in your store.', 'woocommerce' ),
						'public'              => false,
						'show_ui'             => true,
						'capability_type'     => 'shop_coupon',
						'map_meta_cap'        => true,
						'publicly_queryable'  => false,
						'exclude_from_search' => true,
						'show_in_menu'        => current_user_can( 'edit_others_shop_orders' ) ? 'woocommerce' : true,
						'hierarchical'        => false,
						'rewrite'             => false,
						'query_var'           => false,
						'supports'            => array( 'title' ),
						'show_in_nav_menus'   => false,
						'show_in_admin_bar'   => true,
					)
**Tags:** #filter

### woocommerce_register_post_type_shop_order
**Args:** array(
					'labels'              => array(
						'name'                  => __( 'Orders', 'woocommerce' ),
						'singular_name'         => _x( 'Order', 'shop_order post type singular name', 'woocommerce' ),
						'add_new'               => __( 'Add order', 'woocommerce' ),
						'add_new_item'          => __( 'Add new order', 'woocommerce' ),
						'edit'                  => __( 'Edit', 'woocommerce' ),
						'edit_item'             => __( 'Edit order', 'woocommerce' ),
						'new_item'              => __( 'New order', 'woocommerce' ),
						'view_item'             => __( 'View order', 'woocommerce' ),
						'search_items'          => __( 'Search orders', 'woocommerce' ),
						'not_found'             => __( 'No orders found', 'woocommerce' ),
						'not_found_in_trash'    => __( 'No orders found in trash', 'woocommerce' ),
						'parent'                => __( 'Parent orders', 'woocommerce' ),
						'menu_name'             => _x( 'Orders', 'Admin menu name', 'woocommerce' ),
						'filter_items_list'     => __( 'Filter orders', 'woocommerce' ),
						'items_list_navigation' => __( 'Orders navigation', 'woocommerce' ),
						'items_list'            => __( 'Orders list', 'woocommerce' ),
					),
					'description'         => __( 'This is where store orders are stored.', 'woocommerce' ),
					'public'              => false,
					'show_ui'             => true,
					'capability_type'     => 'shop_order',
					'map_meta_cap'        => true,
					'publicly_queryable'  => false,
					'exclude_from_search' => true,
					'show_in_menu'        => current_user_can( 'edit_others_shop_orders' ) ? 'woocommerce' : true,
					'hierarchical'        => false,
					'show_in_nav_menus'   => false,
					'rewrite'             => false,
					'query_var'           => false,
					'supports'            => array( 'title', 'comments', 'custom-fields' ),
					'has_archive'         => false,
				)
**Tags:** #filter

### woocommerce_register_post_type_shop_order_refund
**Args:** array(
					'label'                            => __( 'Refunds', 'woocommerce' ),
					'capability_type'                  => 'shop_order',
					'public'                           => false,
					'hierarchical'                     => false,
					'supports'                         => false,
					'add_order_meta_boxes'             => false,
					'exclude_from_order_count'         => true,
					'exclude_from_order_views'         => false,
					'exclude_from_order_reports'       => false,
					'exclude_from_order_sales_reports' => true,
					'class_name'                       => 'WC_Order_Refund',
					'rewrite'                          => false,
				)
**Tags:** #filter

### woocommerce_save_settings_$CURRENT_TAB
**Tags:** #filter

### woocommerce_save_settings_$CURRENT_TAB_$CURRENT_SECTION
**Tags:** #filter

### woocommerce_screen_ids
**Args:** $screen_ids
**Tags:** #filter

### woocommerce_settings-$GROUP_ID
**Tags:** #filter

### woocommerce_settings_api_form_fields_$THIS->ID
**Tags:** #filter

### woocommerce_settings_api_sanitized_fields_$THIS->ID
**Tags:** #filter

### woocommerce_settings_features
**Params:** bool $disabled
**Tags:** #filter
Filter allowing to add additional settings to the WooCommerce Advanced - Features settings page.

### woocommerce_settings_form_method_tab_$CURRENT_TAB
**Tags:** #filter

### woocommerce_settings_groups
**Params:** WP_REST_Request $request
**Since:** 3.0.0 | **Tags:** #filter
Get all settings groups items.

### woocommerce_settings_pages
**Args:** $settings
**Tags:** #filter

### woocommerce_settings_rest_api
**Params:** array $settings
**Since:** 3.4.0 | **Tags:** #filter
Filter the settings rendered in the Legacy API section of the Advanced settings tab. Core no longer ships any settings in this section; the section itself is only registered when at least one callback is hooked into this filter.

### woocommerce_settings_tabs_array
**Args:** array()
**Tags:** #filter

### woocommerce_shared_settings
**Params:** array $data
**Since:** 5.0.0 | **Tags:** #filter
Filters the array of shared settings. Low level hook for registration of new data late in the cycle. This is deprecated. Instead, use the data api: ```php Automattic\WooCommerce\Blocks\Package::container()->get( Automattic\WooCommerce\Blocks\Assets\AssetDataRegistry::class )->add( $key, $value ) ```

### woocommerce_show_admin_bar_visit_store
**Args:** true
**Tags:** #filter

### woocommerce_show_admin_notice
**Args:** true, $notice
**Tags:** #filter

### woocommerce_tax_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_taxonomy_args_$NAME
**Tags:** #filter

### woocommerce_taxonomy_args_$TAXONOMY_NAME
**Tags:** #filter

### woocommerce_taxonomy_args_$TERM[domain]
**Tags:** #filter

### woocommerce_taxonomy_args_product_cat
**Args:** array(
					'hierarchical'          => true,
					'update_count_callback' => '_wc_term_recount',
					'label'                 => __( 'Categories', 'woocommerce' ),
					'labels'                => array(
						'name'                  => __( 'Product categories', 'woocommerce' ),
						'singular_name'         => __( 'Category', 'woocommerce' ),
						'menu_name'             => _x( 'Categories', 'Admin menu name', 'woocommerce' ),
						'search_items'          => __( 'Search categories', 'woocommerce' ),
						'all_items'             => __( 'All categories', 'woocommerce' ),
						'parent_item'           => __( 'Parent category', 'woocommerce' ),
						'parent_item_colon'     => __( 'Parent category:', 'woocommerce' ),
						'edit_item'             => __( 'Edit category', 'woocommerce' ),
						'update_item'           => __( 'Update category', 'woocommerce' ),
						'add_new_item'          => __( 'Add new category', 'woocommerce' ),
						'new_item_name'         => __( 'New category name', 'woocommerce' ),
						'not_found'             => __( 'No categories found', 'woocommerce' ),
						'item_link'             => __( 'Product Category Link', 'woocommerce' ),
						'item_link_description' => __( 'A link to a product category.', 'woocommerce' ),
						'template_name'         => _x( 'Products by Category', 'Template name', 'woocommerce' ),
					),
					'show_in_rest'          => true,
					'show_ui'               => true,
					'query_var'             => true,
					'capabilities'          => array(
						'manage_terms' => 'manage_product_terms',
						'edit_terms'   => 'edit_product_terms',
						'delete_terms' => 'delete_product_terms',
						'assign_terms' => 'assign_product_terms',
					),
					'rewrite'               => array(
						'slug'         => $permalinks['category_rewrite_slug'],
						'with_front'   => false,
						'hierarchical' => true,
					),
				)
**Tags:** #filter

### woocommerce_taxonomy_args_product_tag
**Args:** array(
					'hierarchical'          => false,
					'update_count_callback' => '_wc_term_recount',
					'label'                 => __( 'Product tags', 'woocommerce' ),
					'labels'                => array(
						'name'                       => __( 'Product tags', 'woocommerce' ),
						'singular_name'              => __( 'Tag', 'woocommerce' ),
						'menu_name'                  => _x( 'Tags', 'Admin menu name', 'woocommerce' ),
						'search_items'               => __( 'Search tags', 'woocommerce' ),
						'all_items'                  => __( 'All tags', 'woocommerce' ),
						'edit_item'                  => __( 'Edit tag', 'woocommerce' ),
						'update_item'                => __( 'Update tag', 'woocommerce' ),
						'add_new_item'               => __( 'Add new tag', 'woocommerce' ),
						'new_item_name'              => __( 'New tag name', 'woocommerce' ),
						'popular_items'              => __( 'Popular tags', 'woocommerce' ),
						'separate_items_with_commas' => __( 'Separate tags with commas', 'woocommerce' ),
						'add_or_remove_items'        => __( 'Add or remove tags', 'woocommerce' ),
						'choose_from_most_used'      => __( 'Choose from the most used tags', 'woocommerce' ),
						'not_found'                  => __( 'No tags found', 'woocommerce' ),
						'item_link'                  => __( 'Product Tag Link', 'woocommerce' ),
						'item_link_description'      => __( 'A link to a product tag.', 'woocommerce' ),
						'template_name'              => _x( 'Products by Tag', 'Template name', 'woocommerce' ),
					),
					'show_in_rest'          => true,
					'show_ui'               => true,
					'query_var'             => true,
					'capabilities'          => array(
						'manage_terms' => 'manage_product_terms',
						'edit_terms'   => 'edit_product_terms',
						'delete_terms' => 'delete_product_terms',
						'assign_terms' => 'assign_product_terms',
					),
					'rewrite'               => array(
						'slug'       => $permalinks['tag_rewrite_slug'],
						'with_front' => false,
					),
				)
**Tags:** #filter

### woocommerce_taxonomy_objects_$NAME
**Tags:** #filter

### woocommerce_taxonomy_objects_$TAXONOMY_NAME
**Tags:** #filter

### woocommerce_taxonomy_objects_$TERM[domain]
**Tags:** #filter

### woocommerce_taxonomy_objects_product_cat
**Args:** array( 'product' )
**Tags:** #filter

### woocommerce_taxonomy_objects_product_tag
**Args:** array( 'product' )
**Tags:** #filter

### woocommerce_widget_settings_sanitize_option
**Args:** $instance[ $key ], $new_instance, $key, $setting
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
