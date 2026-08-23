# WooCommerce Filters: Product

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_add_to_cart_form_action
**Params:** string $action_url
**Since:** 10.0.0 | **Tags:** #filter
Filter the add to cart form action.

### woocommerce_grouped_product_columns
**Args:** array(
					'quantity',
					'label',
					'price',
				), $product
**Tags:** #filter

### woocommerce_grouped_product_list_column_$COLUMN_ID
**Tags:** #filter

### woocommerce_grouped_product_list_link
**Args:** $grouped_product_child->get_permalink(), $grouped_product_child->get_id()
**Tags:** #filter

### woocommerce_out_of_stock_message
**Args:** __( 'This product is currently out of stock and unavailable.', 'woocommerce' )
**Tags:** #filter

### woocommerce_product_$KEY_tab_title
**Tags:** #filter

### woocommerce_product_additional_information_heading
**Args:** __( 'Additional information', 'woocommerce' )
**Tags:** #filter

### woocommerce_product_cross_sells_products_heading
**Args:** __( 'You may be interested in&hellip;', 'woocommerce' )
**Tags:** #filter

### woocommerce_product_description_heading
**Args:** __( 'Description', 'woocommerce' )
**Tags:** #filter

### woocommerce_product_price_class
**Args:** 'price'
**Tags:** #filter

### woocommerce_product_related_products_heading
**Args:** __( 'Related products', 'woocommerce' )
**Tags:** #filter

### woocommerce_product_review_comment_form_args
**Params:** array $comment_form, int $post_id
**Since:** 9.9.0 | **Tags:** #filter
Filters the comment form arguments.

### woocommerce_product_review_list_args
**Args:** array( 'callback' => 'woocommerce_comments' )
**Tags:** #filter

### woocommerce_product_tabs
**Params:** array $tabs
**Since:** 3.3.0 | **Tags:** #filter
Filter the product tabs in the product details block.

### woocommerce_product_thumbnails_columns
**Args:** 4
**Tags:** #filter

### woocommerce_product_upsells_products_heading
**Args:** __( 'You may also like&hellip;', 'woocommerce' )
**Tags:** #filter

### woocommerce_quantity_input_min
**Params:** int|float $quantity, \WC_Product $this
**Since:** 10.1.0 | **Tags:** #filter
Filters the minimum quantity which can be purchased at once.

### woocommerce_reset_variations_link
**Params:** string $button
**Since:** 2.5.0 | **Tags:** #filter
Filters the reset variation button.

### woocommerce_sale_flash
**Args:** '<span class="onsale">' . esc_html__( 'Sale!', 'woocommerce' ) . '</span>', $post, $product
**Tags:** #filter

### woocommerce_single_product_image_gallery_classes
**Args:** array(
		'woocommerce-product-gallery',
		'woocommerce-product-gallery--' . ( $post_thumbnail_id ? 'with-images' : 'without-images' ),
		'woocommerce-product-gallery--columns-' . absint( $columns ),
		'images',
	)
**Tags:** #filter

### woocommerce_single_product_image_thumbnail_html
**Params:** string $html, int $attachment_id
**Since:** 1.6.4 | **Tags:** #filter
Filter product image thumbnail HTML string.

### get_product_search_form
**Args:** ob_get_clean()
**Tags:** #filter

### product_cat_class
**Args:** $classes, $class, $category
**Tags:** #filter

### single_product_archive_thumbnail_size
**Args:** $size
**Tags:** #filter

### wc_product_enable_dimensions_display
**Params:** bool $enable_dimensions_display
**Since:** 2.0.14 | **Tags:** #filter
Filter to customize the display of dimensions for a product in its product page.

### woocommerce_after_output_product_categories
**Args:** ''
**Tags:** #filter

### woocommerce_ajax_variation_threshold
**Args:** 30, $product
**Tags:** #filter

### woocommerce_before_output_product_categories
**Args:** ''
**Tags:** #filter

### woocommerce_catalog_orderby
**Params:** array $catalog_orderby_options
**Since:** 9.7.0 | **Tags:** #filter
Filters the catalog orderby options.

### woocommerce_catalog_orderedby
**Params:** array $orderedby_messages
**Since:** 9.3.0 | **Tags:** #filter
Filters ordered by messages.

### woocommerce_cross_sells_columns
**Args:** $columns
**Tags:** #filter

### woocommerce_cross_sells_order
**Args:** $order
**Tags:** #filter

### woocommerce_cross_sells_orderby
**Args:** $orderby
**Tags:** #filter

### woocommerce_cross_sells_total
**Params:** int $limit
**Since:** 3.0.0 | **Tags:** #filter
Filter the number of cross sell products should on the product page.

### woocommerce_default_catalog_orderby
**Params:** string $default_orderby
**Since:** 1.6.4 | **Tags:** #filter
Filters the default orderby option.

### woocommerce_display_product_attributes
**Params:** array $product_attributes, WC_Product $product
**Since:** 3.6.0. | **Tags:** #filter
Hook: woocommerce_display_product_attributes.

### woocommerce_dropdown_variation_attribute_options_args
**Params:** array $args
**Since:** 2.4.0 | **Tags:** #filter
Output a list of variation attributes for use in the cart forms.

### woocommerce_dropdown_variation_attribute_options_html
**Args:** $html, $args
**Tags:** #filter

### woocommerce_gallery_full_size
**Params:** string $size
**Since:** 2.6.0 | **Tags:** #filter
Filters the size for the full gallery image.

### woocommerce_gallery_image_html_attachment_image_params
**Params:** array $image_attributes
**Since:** 3.3.2 | **Tags:** #filter
Filters the attributes for the image markup.

### woocommerce_gallery_image_size
**Params:** string $size
**Since:** 2.6.0 | **Tags:** #filter
Filters the size for the gallery image.

### woocommerce_gallery_thumbnail_size
**Params:** array $size
**Since:** 2.6.0 | **Tags:** #filter
Filters the size for the gallery thumbnail.

### woocommerce_get_price_html_from_text
**Args:** '<span class="from">' . _x( 'From:', 'min_price', 'woocommerce' ) . ' </span>'
**Tags:** #filter

### woocommerce_get_product_class_include_taxonomies
**Args:** false
**Tags:** #filter

### woocommerce_get_product_subcategories_cache_key
**Args:** 'product-category-hierarchy-' . $parent_id, $parent_id
**Tags:** #filter

### woocommerce_get_stock_html
**Args:** $html, $product
**Tags:** #filter

### woocommerce_loop_product_link
**Args:** get_the_permalink(), $product
**Tags:** #filter

### woocommerce_output_related_products_args
**Args:** $args
**Tags:** #filter

### woocommerce_product_get_rating_html
**Args:** $html, $rating, $count
**Tags:** #filter

### woocommerce_product_loop_end
**Args:** ob_get_clean()
**Tags:** #filter

### woocommerce_product_loop_start
**Args:** ob_get_clean()
**Tags:** #filter

### woocommerce_product_loop_title_classes
**Args:** 'woocommerce-loop-product__title'
**Tags:** #filter

### woocommerce_product_subcategories_args
**Args:** array(
						'parent'       => $parent_id,
						'hide_empty'   => 0,
						'hierarchical' => 1,
						'taxonomy'     => 'product_cat',
						'pad_counts'   => 1,
					)
**Tags:** #filter

### woocommerce_product_subcategories_hide_empty
**Args:** true
**Tags:** #filter

### woocommerce_product_thumbnails_large_size
**Args:** 'full'
**Tags:** #filter

### woocommerce_quantity_input_args
**Params:** array $args, \WC_Product|null $product
**Since:** 2.5.0 | **Tags:** #filter
Filters all quantity input args.

### woocommerce_quantity_input_autocomplete
**Args:** 'off', $product
**Tags:** #filter

### woocommerce_quantity_input_classes
**Args:** array( 'input-text', 'qty', 'text' ), $product
**Tags:** #filter

### woocommerce_quantity_input_inputmode
**Args:** wc_is_stock_amount_integer() ? 'numeric' : 'decimal'
**Tags:** #filter

### woocommerce_quantity_input_max
**Params:** int|float $quantity, \WC_Product $this
**Since:** 10.1.0 | **Tags:** #filter
Filters the maximum quantity which can be purchased at once.

### woocommerce_quantity_input_pattern
**Args:** wc_is_stock_amount_integer() ? '[0-9]*' : ''
**Tags:** #filter

### woocommerce_quantity_input_placeholder
**Args:** '', $product
**Tags:** #filter

### woocommerce_quantity_input_step
**Params:** int|float $step, \WC_Product $this
**Since:** 10.1.0 | **Tags:** #filter
Filters the step for the quantity input for this product.

### woocommerce_quantity_input_type
**Args:** $type
**Tags:** #filter

### woocommerce_related_products_columns
**Args:** $args['columns']
**Tags:** #filter

### woocommerce_single_product_flexslider_enabled
**Args:** get_theme_support( 'wc-product-gallery-slider' )
**Tags:** #filter

### woocommerce_stock_html
**Args:** $html, $availability['availability'], $product
**Tags:** #filter

### woocommerce_upsell_display_args
**Args:** array(
				'posts_per_page' => $limit,
				'orderby'        => $orderby,
				'order'          => $order,
				'columns'        => $columns,
			)
**Tags:** #filter

### woocommerce_upsells_columns
**Args:** isset( $args['columns'] ) ? $args['columns'] : $columns
**Tags:** #filter

### woocommerce_upsells_order
**Args:** isset( $args['order'] ) ? $args['order'] : $order
**Tags:** #filter

### woocommerce_upsells_orderby
**Args:** isset( $args['orderby'] ) ? $args['orderby'] : $orderby
**Tags:** #filter

### woocommerce_upsells_total
**Params:** int $limit
**Since:** 3.0.0 | **Tags:** #filter
Filter the number of upsell products should on the product page.

### woocommerce_variation_option_name
**Params:** string $name, \WP_Term $term, string $taxonomy, \WC_Product $product
**Since:** 10.7.0 | **Tags:** #filter
Filters the variation option name for taxonomy attributes.

### woocommerce_pay_order_product_has_enough_stock
**Params:** \WC_Product $product, \WC_Order $order
**Since:** 9.8.0 | **Tags:** #filter
Filters whether or not the product has enough stock.

### woocommerce_pay_order_product_in_stock
**Params:** \WC_Product $product, \WC_Order $order
**Since:** 9.8.0 | **Tags:** #filter
Filters whether or not the product is in stock for this pay for order.

### woocommerce_product_query_max_rand_cache_count
**Args:** 5
**Tags:** #filter

### woocommerce_after_widget_product_list
**Args:** '</ul>'
**Tags:** #filter

### woocommerce_after_widget_product_review_list
**Args:** '</ul>'
**Tags:** #filter

### woocommerce_before_widget_product_list
**Args:** '<ul class="product_list_widget">'
**Tags:** #filter

### woocommerce_before_widget_product_review_list
**Args:** '<ul class="product_list_widget">'
**Tags:** #filter

### woocommerce_get_filtered_term_product_counts_query
**Params:** array $query
**Since:** 10.9.0 | **Tags:** #filter
Customizes the SQL query that populates product counts in layered navigation.

### woocommerce_price_filter_post_type
**Args:** array( 'product' )
**Tags:** #filter

### woocommerce_price_filter_sql
**Args:** $sql, $meta_query_sql, $tax_query_sql
**Tags:** #filter

### woocommerce_price_filter_widget_tax_class
**Args:** ''
**Tags:** #filter

### woocommerce_product_categories_widget_args
**Args:** $list_args
**Tags:** #filter

### woocommerce_product_categories_widget_dropdown_args
**Args:** wp_parse_args(
						$dropdown_args,
						array(
							'show_count'         => $count,
							'hierarchical'       => $hierarchical,
							'show_uncategorized' => 0,
							'selected'           => $this->current_cat ? $this->current_cat->slug : '',
						)
					)
**Tags:** #filter

### woocommerce_product_categories_widget_main_term
**Args:** $terms[0], $terms
**Tags:** #filter

### woocommerce_product_categories_widget_product_terms_args
**Args:** array(
						'orderby' => 'parent',
						'order'   => 'DESC',
					)
**Tags:** #filter

### woocommerce_product_tag_cloud_widget_args
**Args:** array(
					'taxonomy'                  => $current_taxonomy,
					'topic_count_text_callback' => array( $this, 'topic_count_text' ),
				)
**Tags:** #filter

### woocommerce_products_widget_query_args
**Args:** $query_args
**Tags:** #filter

### woocommerce_recently_viewed_products_widget_query_args
**Args:** $query_args
**Tags:** #filter

### woocommerce_top_rated_products_widget_args
**Args:** array(
				'posts_per_page' => $number,
				'no_found_rows'  => 1,
				'post_status'    => 'publish',
				'post_type'      => 'product',
				'meta_key'       => '_wc_average_rating',
				'orderby'        => 'meta_value_num',
				'order'          => 'DESC',
				'meta_query'     => WC()->query->get_meta_query(),
				'tax_query'      => WC()->query->get_tax_query(),
			)
**Tags:** #filter

### wc_product_pre_lock_on_sku
**Params:** bool|null $locked, WC_Product $product
**Since:** 9.3.0 | **Tags:** #filter
Filter to bail early on the SKU lock query.

### woocommerce_coupon_hold_minutes
**Params:** int $default_hold_time_minutes
**Since:** 3.7.0 | **Tags:** #filter
Filter the tentative hold time in minutes for a coupon before it expires.

### woocommerce_downloadable_product_download_log_insert_data
**Args:** $data
**Tags:** #filter

### woocommerce_downloadable_product_download_log_insert_format
**Args:** $format, $data
**Tags:** #filter

### woocommerce_get_product_id_by_global_unique_id
**Params:** mixed $id, string $global_unique_id
**Since:** 9.1.0 | **Tags:** #filter
Hook woocommerce_get_product_id_by_global_unique_id.

### woocommerce_get_product_id_by_sku
**Args:** $id, $sku
**Tags:** #filter

### woocommerce_get_variation_prices_hash
**Params:** array $price_hash, WC_Product $product, bool $for_display
**Since:** 2.5.0 | **Tags:** #filter
Filters the hash used for caching variation prices. IMPORTANT: see the documentation for the 'woocommerce_variation_prices_price' filter.

### woocommerce_load_product_cogs_is_additive_flag
**Params:** bool $cogs_value_is_additive, WC_Product $product
**Since:** 9.7.0 | **Tags:** #filter
Filter to customize the "Cost of Goods Sold value is additive" flag that gets loaded for a given variable product.

### woocommerce_load_product_cogs_value
**Params:** float $cogs_value, WC_Product $product
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets loaded for a given product.

### woocommerce_new_coupon_data
**Args:** array(
					'post_type'     => 'shop_coupon',
					'post_status'   => $coupon->get_status( 'edit' ) ? $coupon->get_status( 'edit' ) : 'publish',
					'post_author'   => get_current_user_id(),
					'post_title'    => $coupon->get_code( 'edit' ),
					'post_content'  => '',
					'post_excerpt'  => $coupon->get_description( 'edit' ),
					'post_date'     => gmdate( 'Y-m-d H:i:s', $coupon->get_date_created()->getOffsetTimestamp() ),
					'post_date_gmt' => gmdate( 'Y-m-d H:i:s', $coupon->get_date_created()->getTimestamp() ),
				)
**Tags:** #filter

### woocommerce_new_product_data
**Args:** array(
					'post_type'      => 'product',
					'post_status'    => $product->get_status() ? $product->get_status() : ProductStatus::PUBLISH,
					'post_author'    => get_current_user_id(),
					'post_title'     => $product->get_name() ? $product->get_name() : __( 'Product', 'woocommerce' ),
					'post_content'   => $product->get_description(),
					'post_excerpt'   => $product->get_short_description(),
					'post_parent'    => $product->get_parent_id(),
					'comment_status' => $product->get_reviews_allowed() ? 'open' : 'closed',
					'ping_status'    => 'closed',
					'menu_order'     => $product->get_menu_order(),
					'post_password'  => $product->get_post_password( 'edit' ),
					'post_date'      => gmdate( 'Y-m-d H:i:s', $product->get_date_created( 'edit' )->getOffsetTimestamp() ),
					'post_date_gmt'  => gmdate( 'Y-m-d H:i:s', $product->get_date_created( 'edit' )->getTimestamp() ),
					'post_name'      => $product->get_slug( 'edit' ),
				)
**Tags:** #filter

### woocommerce_new_product_variation_data
**Args:** array(
					'post_type'      => 'product_variation',
					'post_status'    => $product->get_status() ? $product->get_status() : ProductStatus::PUBLISH,
					'post_author'    => get_current_user_id(),
					'post_title'     => $product->get_name( 'edit' ),
					'post_excerpt'   => $product->get_attribute_summary( 'edit' ),
					'post_content'   => '',
					'post_parent'    => $product->get_parent_id(),
					'comment_status' => 'closed',
					'ping_status'    => 'closed',
					'menu_order'     => $product->get_menu_order(),
					'post_date'      => gmdate( 'Y-m-d H:i:s', $product->get_date_created( 'edit' )->getOffsetTimestamp() ),
					'post_date_gmt'  => gmdate( 'Y-m-d H:i:s', $product->get_date_created( 'edit' )->getTimestamp() ),
					'post_name'      => $product->get_slug( 'edit' ),
				)
**Tags:** #filter

### woocommerce_product_data_store_cpt_get_products_query
**Args:** $wp_query_args, $query_vars, $this
**Tags:** #filter

### woocommerce_product_pre_search_products
**Args:** false, $term, $type, $include_variations, $all_statuses, $limit
**Tags:** #filter

### woocommerce_product_read_attribute
**Params:** WC_Product_Attribute $attribute, array $meta_value, WC_Product $product
**Since:** 10.6.0 | **Tags:** #filter
Filter product attribute after initialization.

### woocommerce_product_read_download
**Params:** WC_Product_Download $download, array $meta_value, WC_Product $product
**Since:** 10.6.0 | **Tags:** #filter
Filter product download after initialization.

### woocommerce_product_related_posts_query
**Args:** $this->get_related_products_query( $cats_array, $tags_array, $exclude_ids, $limit + 10 ), $product_id, $args
**Tags:** #filter

### woocommerce_product_variation_title
**Args:** $title_suffix ? $title_base . $separator . $title_suffix : $title_base, $product, $title_base, $title_suffix
**Tags:** #filter

### woocommerce_product_variation_title_attributes_separator
**Params:** string $separator, \WC_Product $product
**Since:** 10.2.0 | **Tags:** #filter
Filter the separator used in the product variation title.

### woocommerce_product_variation_title_include_attributes
**Args:** $should_include_attributes, $product
**Tags:** #filter

### woocommerce_save_product_cogs_is_additive_flag
**Params:** bool|null $cogs_value_is_additive, WC_Product $product
**Since:** 9.7.0 | **Tags:** #filter
Filter to customize the "Cost of Goods Sold value is additive" flag that gets saved for a given variable product, or to suppress the saving of the flag (so that custom storage can be used) if null is returned. Note that returning null will suppress any database access (for either saving the flag or deleting it).

### woocommerce_save_product_cogs_value
**Params:** float|null|false $cogs_value, WC_Product $product
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the Cost of Goods Sold value that gets saved for a given product, or to suppress the saving of the value (so that custom storage can be used).

### woocommerce_search_products_post_statuses
**Params:** array $post_statuses
**Since:** 3.7.0 | **Tags:** #filter
Hook woocommerce_search_products_post_statuses.

### woocommerce_update_product_stock_query
**Args:** $sql, $product_id_with_stock, $stock_quantity, 'set'
**Tags:** #filter

### woocommerce_use_legacy_get_variations_price_hash
**Params:** bool $use_legacy, WC_Product $product, bool $for_display
**Since:** 10.5.0 | **Tags:** #filter
Filters whether to use the legacy callback serialization algorithm. By default, WooCommerce will use the legacy algorithm to get the callback signatures for variation price hash calculation. This algorithm serializes the entire callback array as it comes from $wp_filter, which means that for callbacks that are class methods the entire object will be serialized, including the current values of the class variables. This implies that a change in these variables will change the price hash, even if they do not affect the price calculation. This filter allows using CallbackUtil instead, which generates a more stable signature that does not depend on the internal state of objects, but only on the method names and class names. This results in a more consistent and reliable price hash, reducing unnecessary cache misses; but can cause compatibility issues with plugins that rely on the legacy behavior. IMPORTANT: see also the documentation for the 'woocommerce_variation_prices_price' filter.

### woocommerce_variation_prices
**Params:** array $prices_array, WC_Product $product, bool $for_display
**Since:** 3.0.0 | **Tags:** #filter
Filters the variation prices array for a variable product. This filter gives plugins one last chance to modify the variation prices array which has been generated and will be stored locally to the class. This value may differ from the transient cache. It is filtered once before storing locally.

### woocommerce_variation_prices_array
**Params:** array $prices_array, WC_Product $variation, bool $for_display
**Since:** 3.6.0 | **Tags:** #filter
Filter the variation prices array before storing in transient cache. This filter allows developers to modify the variation prices array for each variation during the price calculation process. It's called for each variation individually and can be used to add custom pricing data or modify existing prices.

### woocommerce_variation_prices_price
**Params:** string|float $price, WC_Product $variation, WC_Product $product
**Since:** 3.0.0 | **Tags:** #filter
Filters the active price for a product variation before it is used in price calculations and caching. IMPORTANT: If your filter returns a price that varies by ANY factor (e.g., current user, time of day, user role, cart contents, etc.), you MUST also hook into the 'woocommerce_get_variation_prices_hash' filter to include that factor in the cache key. Otherwise, the wrong price may be cached and displayed to different users or contexts. Example: Applying a per-user discount and adapting the price hash info accordingly: class My_Custom_Pricing { public function __construct() { add_filter( 'woocommerce_variation_prices_price', array( $this, 'apply_user_discount' ), 10, 3 ); add_filter( 'woocommerce_get_variation_prices_hash', array( $this, 'add_user_to_hash' ), 10, 3 ); } public function apply_user_discount( $price, $variation, $product ) { return $price * $this->get_discount_for_user( get_current_user_id() ); } public function add_user_to_hash( $price_hash, $product, $for_display ) { $price_hash[] = get_current_user_id(); return $price_hash; } }

### woocommerce_variation_prices_regular_price
**Params:** string|float $regular_price, WC_Product $variation, WC_Product $product
**Since:** 3.0.0 | **Tags:** #filter
Filters the regular price for a product variation before it is used in price calculations and caching. IMPORTANT: see the documentation for the 'woocommerce_variation_prices_price' filter.

### woocommerce_variation_prices_sale_price
**Params:** string|float $sale_price, WC_Product $variation, WC_Product $product
**Since:** 3.0.0 | **Tags:** #filter
Filters the sale price for a product variation before it is used in price calculations and caching. IMPORTANT: see the documentation for the 'woocommerce_variation_prices_price' filter.

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXbackorders
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXcatalog_visibility
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXpurchase_note
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXsku
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXstock_quantity
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXtax_class
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXweight
**Tags:** #filter

### __experimental_woocommerce_blocks_add_data_attributes_to_block
**Params:** array $allowed_namespaces
**Since:** 5.9.0 | **Tags:** #filter
Filters the list of allowed Block Names This hook defines which block names should have block name and attribute data- attributes appended on render.

### __experimental_woocommerce_blocks_add_data_attributes_to_namespace
**Args:** array()
**Tags:** #filter

### experimental_woocommerce_analytics_variations_additional_clauses
**Params:** array $query_args, SqlQuery $subquery
**Since:** 7.4.0 | **Tags:** #filter
Experimental: Filter the Variations SQL query allowing extensions to add additional SQL clauses.

### experimental_woocommerce_analytics_variations_collection_params
**Params:** array $collection_params
**Since:** 6.5.0 | **Tags:** #filter
Experimental: Filter the list of parameters provided when querying data from the data store.

### experimental_woocommerce_analytics_variations_should_exclude_simple_products
**Params:** array $query_args
**Tags:** #filter
Returns if simple products should be excluded from the report.

### experimental_woocommerce_analytics_variations_stats_collection_params
**Params:** array $collection_params
**Tags:** #filter
Experimental: Filter the list of parameters provided when querying data from the data store.

### experimental_woocommerce_analytics_variations_stats_should_exclude_simple_products
**Params:** array $query_args
**Tags:** #filter
Returns if simple products should be excluded from the report.

### experimental_woocommerce_product_editor_product_template_id_for_product
**Tags:** #filter

### formatted_woocommerce_price
**Params:** float $formatted_price, float $price, int $decimals, string $decimal_separator, string $thousand_separator, float|string $original_price
**Tags:** #filter
Filter formatted price.

### list_product_cats
**Args:** $cat->name, $cat
**Tags:** #filter

### product_attributes_type_selector
**Args:** $attribute_types
**Tags:** #filter

### product_type_options
**Args:** wc_get_default_product_type_options()
**Tags:** #filter

### product_type_selector
**Args:** array(
			ProductType::SIMPLE   => __( 'Simple product', 'woocommerce' ),
			ProductType::GROUPED  => __( 'Grouped product', 'woocommerce' ),
			ProductType::EXTERNAL => __( 'External/Affiliate product', 'woocommerce' ),
			ProductType::VARIABLE => __( 'Variable product', 'woocommerce' ),
		)
**Tags:** #filter

### raw_woocommerce_price
**Params:** float $raw_price, float|string $original_price
**Tags:** #filter
Filter raw price.

### register_taxonomy_product_brand
**Params:** array $args
**Since:** 9.4.0 | **Tags:** #filter
Filter the brand taxonomy.

### rest_pre_insert_product_review
**Params:** array $prepared_review, WP_REST_Request $request
**Tags:** #filter
Filter a product review (comment) before it is inserted via the REST API. Allows modification of the comment right before it is inserted via `wp_insert_comment`.

### rest_preprocess_product_review
**Args:** $prepared_review, $request
**Tags:** #filter

### rest_product_review_trashable
**Params:** boolean $supports_trash, WP_Post $product_review
**Tags:** #filter
Filter whether a product review is trashable. Return false to disable trash support for the product review.

### update_woo_com_subscription_details
**Params:** array $item, array $data, int $product_id
**Since:** 8.7.0 | **Tags:** #filter
Filters the Woo plugin data before saving it in transient used for updates.

### wc_get_price_decimal_separator
**Args:** get_option( 'woocommerce_price_decimal_sep' )
**Tags:** #filter

### wc_get_price_decimals
**Args:** get_option( 'woocommerce_price_num_decimals', 2 )
**Tags:** #filter

### wc_get_price_thousand_separator
**Args:** get_option( 'woocommerce_price_thousand_sep' )
**Tags:** #filter

### wc_price
**Params:** string $return, string $price, array $args, float $unformatted_price, float|string $original_price
**Tags:** #filter
Filters the string of price markup.

### wc_price_args
**Params:** float $price, array $args
**Tags:** #filter
Format the price with a currency symbol.

### wc_product_dimensions_enabled
**Args:** true
**Tags:** #filter

### wc_product_has_global_unique_id
**Params:** boolean $global_unique_id_found, int $product_id, string $sku
**Since:** 9.1.0 | **Tags:** #filter
Gives plugins an opportunity to verify Unique ID uniqueness themselves.

### wc_product_has_unique_sku
**Params:** bool|null $sku_found, int $product_id, string $sku
**Since:** 10.5.0 | **Tags:** #filter
Gives plugins an opportunity to verify SKU uniqueness themselves. Filter added to keep backwards compatibility with `wc_product_has_unique_sku()`. See: https://github.com/woocommerce/woocommerce/pull/62628

### wc_product_post_type_link_product_cat
**Params:** WP_Term $deepest_term, WP_Term[] $terms, WP_Post $post
**Since:** 2.4.0 | **Tags:** #filter
Filter the product category used for the product permalink. By default, the deepest category (most ancestors) is selected. Prior to 9.9.0, categories were sorted by parent term ID descending, then term ID ascending. This filter allows customization of which category is used in the product permalink.

### wc_product_pre_has_global_unique_id
**Params:** bool|null $has_global_unique_id, int $product_id, string $sku
**Since:** 9.1.0 | **Tags:** #filter
Gives plugins an opportunity to verify Unique ID uniqueness themselves.

### wc_product_pre_has_unique_sku
**Params:** bool|null $has_unique_sku, int $product_id, string $sku
**Since:** 10.5.0 | **Tags:** #filter
Gives plugins an opportunity to verify SKU uniqueness themselves. Filter added to keep backwards compatibility with `wc_product_has_unique_sku()`. See: https://github.com/woocommerce/woocommerce/pull/62628

### wc_product_sku_enabled
**Args:** true
**Tags:** #filter

### wc_product_weight_enabled
**Args:** true
**Tags:** #filter

### woocommerce_add_to_cart_product_id
**Args:** absint( $_POST['product_id'] )
**Tags:** #filter

### woocommerce_adjust_non_base_location_prices
**Params:** bool $adjust_non_base_location_prices
**Since:** 2.4.7 | **Tags:** #filter
Filters if taxes should be removed from locations outside the store base location. The woocommerce_adjust_non_base_location_prices filter can stop base taxes being taken off when dealing with out of base locations. e.g. If a product costs 10 including tax, all users will pay 10 regardless of location and taxes.

### woocommerce_analytics_coupons_query_args
**Args:** array(
					'orderby'       => 'orders_count',
					'order'         => 'desc',
					'after'         => $after,
					'before'        => $before,
					'per_page'      => $per_page,
					'extended_info' => true,
				)
**Tags:** #filter

### woocommerce_analytics_coupons_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_coupons_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_products_query_args
**Args:** array(
					'orderby'       => 'items_sold',
					'order'         => 'desc',
					'after'         => $after,
					'before'        => $before,
					'per_page'      => $per_page,
					'extended_info' => true,
				)
**Tags:** #filter

### woocommerce_analytics_products_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_products_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_products_stats_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_stock_stats_query
**Args:** $results
**Tags:** #filter

### woocommerce_analytics_variations_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_variations_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_variations_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_variations_stats_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_apply_individual_use_coupon
**Params:** array $coupons, \WC_Coupon $coupon, array $applied_coupons
**Since:** 2.6.0 | **Tags:** #filter
Filter coupons to remove when applying an individual use coupon.

### woocommerce_apply_with_individual_use_coupon
**Params:** boolean $apply_with_individual_use_coupon, \WC_Coupon $coupon, \WC_Coupon $individual_use_coupon, array $applied_coupons
**Since:** 2.6.0 | **Tags:** #filter
Filters if a coupon can be applied alongside other individual use coupons.

### woocommerce_available_variation
**Args:** array(
				'attributes'            => $variation->get_variation_attributes(),
				'availability_html'     => wc_get_stock_html( $variation ),
				'backorders_allowed'    => $variation->backorders_allowed(),
				'dimensions'            => $variation->get_dimensions( false ),
				'dimensions_html'       => wc_format_dimensions( $variation->get_dimensions( false ) ),
				'display_price'         => wc_get_price_to_display( $variation ),
				'display_regular_price' => wc_get_price_to_display( $variation, array( 'price' => $variation->get_regular_price() ) ),
				'gallery_image_ids'     => $variation_gallery_image_ids,
				'gallery_images_html'   => $variation_gallery_html,
				'image'                 => wc_get_product_attachment_props( $selected_image_id ),
				'image_id'              => $selected_image_id,
				'is_downloadable'       => $variation->is_downloadable(),
				'is_in_stock'           => $variation->is_in_stock(),
				'is_purchasable'        => $variation->is_purchasable(),
				'is_sold_individually'  => $variation->is_sold_individually() ? 'yes' : 'no',
				'is_virtual'            => $variation->is_virtual(),
				'max_qty'               => 0 < $variation->get_max_purchase_quantity() ? $variation->get_max_purchase_quantity() : '',
				'min_qty'               => $variation->get_min_purchase_quantity(),
				'price_html'            => $show_variation_price ? '<span class="price">' . $variation->get_price_html() . '</span>' : '',
				'sku'                   => $variation->get_sku(),
				'variation_description' => wc_format_content( $variation->get_description() ),
				'variation_id'          => $variation->get_id(),
				'variation_is_active'   => $variation->variation_is_active(),
				'variation_is_visible'  => $variation->variation_is_visible(),
				'weight'                => $variation->get_weight(),
				'weight_html'           => wc_format_weight( $variation->get_weight() ),
			), $this, $variation
**Tags:** #filter

### woocommerce_backordered_item_meta_name
**Params:** string $backorder_meta_key, WC_Order_Item_Product $item
**Since:** 9.9.0 | **Tags:** #filter
Filter the backorder meta key. Make sure to use the same filter as used in set_backorder_meta().

### woocommerce_blocks_product_filters_selected_items
**Args:** array(), $filter_params
**Tags:** #filter

### woocommerce_blocks_product_grid_add_to_cart_attributes
**Params:** array $attributes, WC_Product $product
**Since:** 8.6.0 | **Tags:** #filter
Filter to manipulate (add/modify/remove) attributes in the HTML code of the generated add to cart button.

### woocommerce_blocks_product_grid_is_cacheable
**Params:** boolean $is_cacheable, array $query_args
**Since:** 2.5.0 | **Tags:** #filter
Filters whether or not the product grid is cacheable.

### woocommerce_blocks_product_grid_item_html
**Params:** string $html, array $data, \WC_Product $product
**Since:** 2.2.0 | **Tags:** #filter
Filters the HTML for products in the grid.

### woocommerce_breadcrumb_product_terms_args
**Params:** array $args
**Since:** 9.5.0 | **Tags:** #filter
Filters the arguments used to fetch product terms for breadcrumbs.

### woocommerce_bulk_edit_save_price_product_types
**Params:** array $product_types
**Since:** 3.0.0 | **Tags:** #filter
Handle price - remove dates and set to lowest.

### woocommerce_bulk_edit_variations_need_children
**Args:** true
**Tags:** #filter

### woocommerce_coupon_code
**Params:** string $value
**Since:** 3.0.0 | **Tags:** #filter
Format a coupon code.

### woocommerce_coupon_code_generator_character_length
**Args:** 8
**Tags:** #filter

### woocommerce_coupon_code_generator_characters
**Args:** 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
**Tags:** #filter

### woocommerce_coupon_code_generator_prefix
**Args:** ''
**Tags:** #filter

### woocommerce_coupon_code_generator_suffix
**Args:** ''
**Tags:** #filter

### woocommerce_coupon_custom_discounts_array
**Args:** $this->discounts[ $coupon->get_code() ], $coupon
**Tags:** #filter

### woocommerce_coupon_data_tabs
**Args:** array(
						'general'           => array(
							'label'  => __( 'General', 'woocommerce' ),
							'target' => 'general_coupon_data',
							'class'  => 'general_coupon_data',
						),
						'usage_restriction' => array(
							'label'  => __( 'Usage restriction', 'woocommerce' ),
							'target' => 'usage_restriction_coupon_data',
							'class'  => '',
						),
						'usage_limit'       => array(
							'label'  => __( 'Usage limits', 'woocommerce' ),
							'target' => 'usage_limit_coupon_data',
							'class'  => '',
						),
					)
**Tags:** #filter

### woocommerce_coupon_discount_amount_html
**Args:** $discount_amount_html, $coupon
**Tags:** #filter

### woocommerce_coupon_discount_types
**Args:** array(
			'percent'       => __( 'Percentage discount', 'woocommerce' ),
			'fixed_cart'    => __( 'Fixed cart discount', 'woocommerce' ),
			'fixed_product' => __( 'Fixed product discount', 'woocommerce' ),
		)
**Tags:** #filter

### woocommerce_coupon_error
**Params:** string $error_message, int $error_code, WC_Coupon $coupon
**Tags:** #filter
Filter the coupon error message.

### woocommerce_coupon_get_apply_quantity
**Args:** $apply_quantity, $item, $coupon, $this
**Tags:** #filter

### woocommerce_coupon_get_discount_amount
**Args:** NumberUtil::round( min( $discount, $discounting_amount ), wc_get_rounding_precision() ), $discounting_amount, $cart_item, $single, $this
**Tags:** #filter

### woocommerce_coupon_get_items_to_apply
**Params:** array $items_to_apply, WC_Coupon $coupon, WC_Discounts $this
**Since:** 8.8.0 | **Tags:** #filter
Filters the items that a coupon should be applied to. This filter allows you to modify the items that a coupon will be applied to before the discount calculations take place.

### woocommerce_coupon_get_items_to_validate
**Args:** $this->get_items(), $this
**Tags:** #filter

### woocommerce_coupon_is_valid
**Args:** true, $coupon, $this
**Tags:** #filter

### woocommerce_coupon_is_valid_for_cart
**Args:** $this->is_type( wc_get_cart_coupon_types() ), $this
**Tags:** #filter

### woocommerce_coupon_is_valid_for_product
**Params:** WC_Product $product, array $values
**Tags:** #filter
Check if a coupon is valid for a product.

### woocommerce_coupon_message
**Args:** $msg, $msg_code, $this
**Tags:** #filter

### woocommerce_coupon_sort
**Args:** $coupon->sort, $coupon
**Tags:** #filter

### woocommerce_coupon_validate_expiry_date
**Params:** WC_Coupon $coupon
**Since:** 3.2.0 | **Tags:** #filter
Ensure coupon date is valid or throw exception.

### woocommerce_coupon_validate_maximum_amount
**Args:** $coupon->get_maximum_amount() < $subtotal, $coupon
**Tags:** #filter

### woocommerce_coupon_validate_minimum_amount
**Args:** $coupon->get_minimum_amount() > $subtotal, $coupon, $subtotal
**Tags:** #filter

### woocommerce_coupon_validate_user_usage_limit
**Args:** $coupon->get_usage_limit_per_user() > 0, $user_id, $coupon, $this
**Tags:** #filter

### woocommerce_coupons_enabled
**Args:** 'yes' === get_option( 'woocommerce_enable_coupons' )
**Tags:** #filter

### woocommerce_csv_product_import_mapped_columns
**Args:** $headers, $raw_headers
**Tags:** #filter

### woocommerce_csv_product_import_mapping_default_columns
**Args:** $default_columns, $raw_headers
**Tags:** #filter

### woocommerce_csv_product_import_mapping_options
**Args:** $options, $item
**Tags:** #filter

### woocommerce_csv_product_import_mapping_special_columns
**Args:** array(
						/* translators: %d: Attribute number */
						__( 'Attribute %d name', 'woocommerce' ) => 'attributes:name',
						/* translators: %d: Attribute number */
						__( 'Attribute %d value(s)', 'woocommerce' ) => 'attributes:value',
						/* translators: %d: Attribute number */
						__( 'Attribute %d visible', 'woocommerce' ) => 'attributes:visible',
						/* translators: %d: Attribute number */
						__( 'Attribute %d global', 'woocommerce' ) => 'attributes:taxonomy',
						/* translators: %d: Attribute number */
						__( 'Attribute %d default', 'woocommerce' ) => 'attributes:default',
						/* translators: %d: Download number */
						__( 'Download %d ID', 'woocommerce' ) => 'downloads:id',
						/* translators: %d: Download number */
						__( 'Download %d name', 'woocommerce' ) => 'downloads:name',
						/* translators: %d: Download number */
						__( 'Download %d URL', 'woocommerce' ) => 'downloads:url',
						/* translators: %d: Meta number */
						__( 'Meta: %s', 'woocommerce' ) => 'meta:',
					), $raw_headers
**Tags:** #filter

### woocommerce_csv_product_import_valid_filetypes
**Args:** array(
				'csv' => 'text/csv',
				'txt' => 'text/plain',
			)
**Tags:** #filter

### woocommerce_default_catalog_orderby_options
**Params:** string $value
**Tags:** #filter
Sanitize the catalog orderby setting.

### woocommerce_delete_variations_on_product_type_change
**Params:** WC_Product $product, string $to
**Since:** 5.0.0 | **Tags:** #filter
Filter to prevent variations from being deleted while switching from a variable product type to a variable product type.

### woocommerce_dimension_units
**Params:** array $dimension_units
**Since:** 10.4.0 | **Tags:** #filter
Filter the available dimension units.

### woocommerce_downloadable_product_name
**Args:** $download_file['name'], $_product, $result->download_id, $file_number
**Tags:** #filter

### woocommerce_duplicate_product_capability
**Args:** 'manage_woocommerce'
**Tags:** #filter

### woocommerce_duplicate_product_exclude_children
**Args:** false, $product
**Tags:** #filter

### woocommerce_duplicate_product_exclude_meta
**Params:** array $exclude_meta, array $existing_meta_keys
**Since:** 2.6 | **Tags:** #filter
Filter to allow us to exclude meta keys from product duplication..

### woocommerce_empty_price_html
**Args:** '', $this
**Tags:** #filter

### woocommerce_exporter_product_types
**Params:** array $product_types
**Since:** 5.1.0 | **Tags:** #filter
Allow third-parties to filter the exportable product types.

### woocommerce_format_dimensions
**Args:** $dimension_string, $dimensions
**Tags:** #filter

### woocommerce_format_localized_price
**Params:** string $value
**Tags:** #filter
Format a price with WC Currency Locale settings.

### woocommerce_format_price_range
**Args:** $price, $from, $to
**Tags:** #filter

### woocommerce_format_sale_price
**Args:** $price, $regular_price, $sale_price
**Tags:** #filter

### woocommerce_format_stock_quantity
**Params:** int $stock_quantity, WC_Product $product
**Since:** 3.0.0 | **Tags:** #filter
Format the stock quantity ready for display.

### woocommerce_format_weight
**Args:** $weight_string, $weight
**Tags:** #filter

### woocommerce_fulfillments_auto_fulfill_products
**Params:** array $auto_fulfill_items, \WC_Order $order
**Since:** 10.1.0 | **Tags:** #filter
Filter to get the list of the item, or variant ID's that should be auto-fulfilled.

### woocommerce_get_catalog_ordering_args
**Args:** $args, $orderby, $order
**Tags:** #filter

### woocommerce_get_coupon_id_from_code
**Args:** absint( current( $ids ) ), $code, $exclude
**Tags:** #filter

### woocommerce_get_discounted_price
**Args:** wc_remove_number_precision( $item->total ), $item->object, $this->cart
**Tags:** #filter

### woocommerce_get_min_max_price_meta_query
**Args:** array(
			'key'     => '_price',
			'value'   => array( $current_min_price, $current_max_price ),
			'compare' => 'BETWEEN',
			'type'    => 'DECIMAL(10,' . wc_get_price_decimals() . ')',
		), $args
**Tags:** #filter

### woocommerce_get_price_excluding_tax
**Args:** $return_price, $qty, $product
**Tags:** #filter

### woocommerce_get_price_html
**Args:** $price, $this
**Tags:** #filter

### woocommerce_get_price_html_from_to
**Args:** wc_format_sale_price( $from, $to ), $from, $to, $this
**Tags:** #filter

### woocommerce_get_price_including_tax
**Args:** $return_price, $qty, $product
**Tags:** #filter

### woocommerce_get_price_suffix
**Args:** $html, $this, $price, $qty
**Tags:** #filter

### woocommerce_get_product_cogs_total_value
**Params:** float $total_value, WC_Product $product
**Since:** 9.5.0 | **Tags:** #filter
Filter to customize the total Cost of Goods Sold value that get_cogs_total_value returns for a given product.

### woocommerce_get_product_from_item
**Params:** WC_Product|false $product, WC_Order_Item_Product $line_item, WC_Order $order
**Since:** 2.7.0 | **Tags:** #filter
Modifies the product object returned by \WC_Order_Item_Product::get_product.

### woocommerce_get_product_terms
**Args:** _wc_get_cached_product_terms( $product_id, $taxonomy, $args ), $product_id, $taxonomy, $args
**Tags:** #filter

### woocommerce_get_related_product_cat_terms
**Args:** wc_get_product_term_ids( $product_id, 'product_cat' ), $product_id
**Tags:** #filter

### woocommerce_get_related_product_tag_terms
**Args:** wc_get_product_term_ids( $product_id, 'product_tag' ), $product_id
**Tags:** #filter

### woocommerce_get_shop_coupon_data
**Args:** false, $data, $this
**Tags:** #filter

### woocommerce_get_variation_price
**Args:** $price, $this, $min_or_max, $for_display
**Tags:** #filter

### woocommerce_get_variation_regular_price
**Args:** $price, $this, $min_or_max, $for_display
**Tags:** #filter

### woocommerce_get_variation_sale_price
**Args:** $price, $this, $min_or_max, $for_display
**Tags:** #filter

### woocommerce_grouped_empty_price_html
**Args:** '', $this
**Tags:** #filter

### woocommerce_grouped_free_price_html
**Args:** __( 'Free!', 'woocommerce' ), $this
**Tags:** #filter

### woocommerce_grouped_price_html
**Args:** $price . $this->get_price_suffix(), $this, $child_prices
**Tags:** #filter

### woocommerce_hide_invisible_variations
**Params:** bool $hide, int $product_id, WC_Product_Variation $variation
**Since:** 2.6.8 | **Tags:** #filter
Filter 'woocommerce_hide_invisible_variations' to optionally hide invisible variations (disabled variations and variations with empty price).

### woocommerce_inventory_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_is_attribute_in_product_name
**Args:** $is_in_name, $attribute, $name
**Tags:** #filter

### woocommerce_is_downloadable
**Args:** true === $this->get_downloadable(), $this
**Tags:** #filter

### woocommerce_is_virtual
**Args:** true === $this->get_virtual(), $this
**Tags:** #filter

### woocommerce_json_search_found_product_attribute_terms
**Params:** array $terms, string $taxonomy
**Since:** 7.0.0 | **Tags:** #filter
Filter the product attribute terms search results.

### woocommerce_json_search_found_product_categories
**Params:** array $found_product_categories, string $search_text
**Since:** 7.0.0 | **Tags:** #filter
Filter the product category search results.

### woocommerce_json_search_found_products
**Args:** $products
**Tags:** #filter

### woocommerce_max_terms_displayed_in_attributes_page
**Args:** 100
**Since:** 6.9.0 | **Tags:** #filter
Filters the maximum number of terms that will be displayed for each taxonomy in the Attributes page.

### woocommerce_pos_catalog_map_product
**Params:** array $row, WC_Product $product
**Since:** 10.5.0 | **Tags:** #filter
Filter mapped catalog product data.

### woocommerce_pre_product_filter_data
**Params:** array $results, string $filter_type, array $query_vars, array $extra
**Since:** 9.9.0 | **Tags:** #filter
Allows offloading the filter data to external services like Elasticsearch.

### woocommerce_prevent_adjust_line_item_product_stock
**Params:** bool $prevent, WC_Order_Item $item, int $item_quantity
**Since:** 3.7.1 | **Tags:** #filter
Prevent adjust line item product stock.

### woocommerce_price_ex_tax_amount
**Args:** $tax_amount, $key, $rate, $price
**Tags:** #filter

### woocommerce_price_format
**Args:** $format, $currency_pos
**Tags:** #filter

### woocommerce_price_inc_tax_amount
**Args:** $non_compound_price - ( $non_compound_price / ( 1 + ( $compound_rate / 100 ) ) ), $key, $rates[ $key ], $price
**Tags:** #filter

### woocommerce_price_trim_zeros
**Args:** false
**Tags:** #filter

### woocommerce_prices_include_tax
**Args:** get_option( 'woocommerce_prices_include_tax' ) === 'yes'
**Tags:** #filter

### woocommerce_product_add_to_cart_aria_describedby
**Params:** string $var, WC_Product $this
**Since:** 7.8.0 | **Tags:** #filter
Filter the aria-describedby description for the add to cart button.

### woocommerce_product_add_to_cart_description
**Args:** sprintf( __( 'Read more about &ldquo;%s&rdquo;', 'woocommerce' ), $this->get_name() ), $this
**Tags:** #filter

### woocommerce_product_add_to_cart_success_message
**Params:** string $text, WC_Product_Simple $this
**Since:** 9.2.0 | **Tags:** #filter
Filter product add to cart success message.

### woocommerce_product_add_to_cart_text
**Args:** __( 'Read more', 'woocommerce' ), $this
**Tags:** #filter

### woocommerce_product_add_to_cart_url
**Args:** $this->get_permalink(), $this
**Tags:** #filter

### woocommerce_product_allow_backorder_use_radio
**Args:** true
**Tags:** #filter

### woocommerce_product_attribute_term_name
**Args:** $selected_term->name, $selected_term
**Tags:** #filter

### woocommerce_product_attribute_terms
**Params:** array $args
**Since:** 3.4.0 | **Tags:** #filter
Filter the product attribute term arguments used for search.

### woocommerce_product_attributes_filterer_hide_out_of_stock
**Params:** bool $option_value
**Since:** 9.8.0. | **Tags:** #filter
Filters the woocommerce_hide_out_of_stock_items option to override the default behavior in product filtering by attribute.

### woocommerce_product_backorders_allowed
**Args:** ( 'yes' === $this->get_backorders() || 'notify' === $this->get_backorders() ), $this->get_id(), $this
**Tags:** #filter

### woocommerce_product_backorders_require_notification
**Args:** ( $this->managing_stock() && 'notify' === $this->get_backorders() ), $this
**Tags:** #filter

### woocommerce_product_brand_filter_threshold
**Params:** int $value
**Since:** 9.4.0 | **Tags:** #filter
Filter the brands threshold count.

### woocommerce_product_brands_output
**Params:** string $brand_output, array $terms, int $post_id
**Since:** 9.8.0 | **Tags:** #filter
Filter the brand output in product meta.

### woocommerce_product_categories
**Args:** get_terms( 'product_cat', $args )
**Tags:** #filter

### woocommerce_product_category_filter_threshold
**Args:** 100
**Tags:** #filter

### woocommerce_product_category_metabox_search_threshold
**Params:** number $threshold
**Since:** 7.6.0 | **Tags:** #filter
Filters the category metabox search threshold, for when to render the typeahead field.

### woocommerce_product_class
**Params:** string $classname, string $product_type, string $context, int $product_id
**Since:** 3.0.0 | **Tags:** #filter
Filter the product class name.

### woocommerce_product_coupon_types
**Args:** array( 'fixed_product', 'percent' )
**Tags:** #filter

### woocommerce_product_crosssell_ids
**Args:** $this->get_cross_sell_ids(), $this
**Tags:** #filter

### woocommerce_product_csv_importer_args
**Args:** $args, $importer_class
**Tags:** #filter

### woocommerce_product_csv_importer_class
**Params:** string $file, array $args
**Tags:** #filter
Get importer instance.

### woocommerce_product_csv_importer_steps
**Args:** $default_steps
**Tags:** #filter

### woocommerce_product_data_tabs
**Args:** array(
				'general'        => array(
					'label'    => __( 'General', 'woocommerce' ),
					'target'   => 'general_product_data',
					'class'    => array( 'hide_if_grouped' ),
					'priority' => 10,
				),
				'inventory'      => array(
					'label'    => __( 'Inventory', 'woocommerce' ),
					'target'   => 'inventory_product_data',
					'class'    => array( 'show_if_simple', 'show_if_variable', 'show_if_grouped', 'show_if_external' ),
					'priority' => 20,
				),
				'shipping'       => array(
					'label'    => __( 'Shipping', 'woocommerce' ),
					'target'   => 'shipping_product_data',
					'class'    => array( 'hide_if_virtual', 'hide_if_grouped', 'hide_if_external' ),
					'priority' => 30,
				),
				'linked_product' => array(
					'label'    => __( 'Linked Products', 'woocommerce' ),
					'target'   => 'linked_product_data',
					'class'    => array(),
					'priority' => 40,
				),
				'attribute'      => array(
					'label'    => __( 'Attributes', 'woocommerce' ),
					'target'   => 'product_attributes',
					'class'    => array(),
					'priority' => 50,
				),
				'variations'     => array(
					'label'    => __( 'Variations', 'woocommerce' ),
					'target'   => 'variable_product_options',
					'class'    => array( 'show_if_variable' ),
					'priority' => 60,
				),
				'advanced'       => array(
					'label'    => __( 'Advanced', 'woocommerce' ),
					'target'   => 'advanced_product_data',
					'class'    => array(),
					'priority' => 70,
				),
			)
**Tags:** #filter

### woocommerce_product_default_attributes
**Args:** $this->get_default_attributes(), $this
**Tags:** #filter

### woocommerce_product_details_hooked_blocks
**Args:** []
**Tags:** #filter

### woocommerce_product_dimensions
**Args:** wc_format_dimensions( $this->get_dimensions( false ) ), $this
**Tags:** #filter

### woocommerce_product_downloads_approved_directory_validation_for_shortcodes
**Params:** bool $should_validate
**Tags:** #filter
Controls whether shortcodes should be resolved and validated using the Approved Download Directory feature.

### woocommerce_product_editor_product_templates
**Tags:** #filter

### woocommerce_product_empty_cogs_html
**Params:** string $html, WC_Product $product
**Since:** 9.8.0 | **Tags:** #filter
Filter to customize how an empty Cost of Goods Sold value for a product gets rendered to HTML.

### woocommerce_product_export_$THIS->EXPORT_TYPE_column_$COLUMN_ID
**Tags:** #filter

### woocommerce_product_export_$THIS->EXPORT_TYPE_default_columns
**Tags:** #filter

### woocommerce_product_export_$THIS->EXPORT_TYPE_query_args
**Tags:** #filter

### woocommerce_product_export_meta_value
**Args:** $meta->value, $meta, $product, $row
**Tags:** #filter

### woocommerce_product_export_row_data
**Params:** array $row, WC_Product $product, WC_Product_CSV_Exporter $exporter
**Since:** 3.1.0 | **Tags:** #filter
Allow third-party plugins to filter the data in a single row of the exported CSV file.

### woocommerce_product_export_skip_meta_keys
**Args:** array(), $product
**Tags:** #filter

### woocommerce_product_feed_args
**Params:** array $query_args, IntegrationInterface $integration
**Since:** 10.5.0 | **Tags:** #filter
Allows the base arguments for querying products for product feeds to be changed. Variable products are not included by default, as their variations will be included.

### woocommerce_product_feed_scheduled_timeout
**Params:** int $stuck_time
**Since:** 10.5.0 | **Tags:** #filter
Allows the timeout for a feed to remain in `scheduled` state to be changed. Past this point Action Scheduler is typically stuck and the job is regenerated.

### woocommerce_product_feed_time
**Params:** int $time, FeedInterface $feed
**Since:** 10.5.0 | **Tags:** #filter
Allows the current time to be overridden before a feed is stored.

### woocommerce_product_file
**Args:** $file, $this, $download_id
**Tags:** #filter

### woocommerce_product_file_download_path
**Args:** $file_path, $this, $download_id
**Tags:** #filter

### woocommerce_product_filter_data
**Params:** array $results, string $filter_type, array $query_vars, array $extra
**Since:** 9.9.0 | **Tags:** #filter
Filters the product filter data before it is returned.

### woocommerce_product_filters
**Args:** $output
**Tags:** #filter

### woocommerce_product_form_templates
**Tags:** #filter

### woocommerce_product_get_cogs_html
**Params:** string $html, float $value, WC_Product $product
**Since:** 9.8.0 | **Tags:** #filter
Filter to customize how the Cost of Goods Sold value for a product gets rendered to HTML.

### woocommerce_product_get_image
**Args:** $image, $this, $size, $attr, $placeholder, $image
**Tags:** #filter

### woocommerce_product_has_options
**Args:** false, $this
**Tags:** #filter

### woocommerce_product_image_loading_attr
**Params:** string $loading_attr, int $image_id
**Since:** 10.6.0 | **Tags:** #filter
Filters the loading attribute for product images. Allowed values are 'lazy', 'eager', and 'auto'. Any other value will result in default browser behavior.

### woocommerce_product_import_batch_size
**Args:** 30
**Tags:** #filter

### woocommerce_product_import_get_product_object
**Args:** $product, $data
**Tags:** #filter

### woocommerce_product_import_image_separator
**Args:** ', '
**Tags:** #filter

### woocommerce_product_import_pre_insert_product_object
**Args:** $object, $data
**Tags:** #filter

### woocommerce_product_import_process_item_data
**Args:** $data
**Tags:** #filter

### woocommerce_product_importer_default_time_limit
**Args:** 20
**Tags:** #filter

### woocommerce_product_importer_formatting_callbacks
**Args:** $callbacks, $this
**Tags:** #filter

### woocommerce_product_importer_memory_exceeded
**Args:** $return
**Tags:** #filter

### woocommerce_product_importer_parsed_data
**Params:** array $parsed_data, WC_Product_Importer $importer
**Tags:** #filter
Filter product importer parsed data.

### woocommerce_product_importer_pre_expand_data
**Params:** array $data
**Tags:** #filter
Expand special and internal data into the correct formats for the product CRUD.

### woocommerce_product_importer_read_attribute
**Params:** WC_Product_Attribute $attribute_object, array $attribute, WC_Product $product
**Since:** 10.6.0 | **Tags:** #filter
Filter product attribute after initialization.

### woocommerce_product_importer_time_exceeded
**Args:** $return
**Tags:** #filter

### woocommerce_product_is_in_stock
**Params:** bool $in_stock, WC_Product $product
**Since:** 2.7.0 | **Tags:** #filter
Filters whether a product is in stock.

### woocommerce_product_is_on_sale
**Args:** $on_sale, $this
**Tags:** #filter

### woocommerce_product_is_taxable
**Params:** bool $taxable, WC_Product $product
**Since:** 2.7.0 | **Tags:** #filter
Filters whether a product is taxable.

### woocommerce_product_is_visible
**Args:** $visible, $this->get_id()
**Tags:** #filter

### woocommerce_product_needs_shipping
**Args:** ! $this->is_virtual(), $this
**Tags:** #filter

### woocommerce_product_object_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_product_object_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_product_parent
**Args:** absint( $this->get_post_data()->post_parent ), $this
**Tags:** #filter

### woocommerce_product_post_type_link_parent_category_only
**Params:** bool $use_parent_only
**Since:** 2.6.5 | **Tags:** #filter
Filter whether to use only the top-level parent category in the product permalink. When true, only the top-level ancestor category slug is used instead of the full category hierarchy path (e.g., 'parent' instead of 'parent/child/grandchild').

### woocommerce_product_query_meta_query
**Args:** $meta_query, $this
**Tags:** #filter

### woocommerce_product_query_tax_query
**Args:** $tax_query, $this
**Tags:** #filter

### woocommerce_product_recount_terms
**Args:** true
**Tags:** #filter

### woocommerce_product_related_posts_force_display
**Args:** false, $product_id
**Tags:** #filter

### woocommerce_product_related_posts_relate_by_category
**Args:** true, $product_id
**Tags:** #filter

### woocommerce_product_related_posts_relate_by_tag
**Args:** true, $product_id
**Tags:** #filter

### woocommerce_product_related_posts_shuffle
**Args:** true
**Tags:** #filter

### woocommerce_product_reviews_is_product_review_or_reply
**Params:** bool $is_review_or_reply, WP_Comment|mixed $object
**Since:** 6.7.0 | **Tags:** #filter
Filters whether the object is a review or a reply to a review.

### woocommerce_product_reviews_list_table
**Params:** string $output, ReviewsListTable $reviews_list_table
**Since:** 6.7.0 | **Tags:** #filter
Filters the contents of the product reviews list table output.

### woocommerce_product_reviews_list_table_item_types
**Args:** array(
				'all'     => __( 'All types', 'woocommerce' ),
				'comment' => __( 'Replies', 'woocommerce' ),
				'review'  => __( 'Reviews', 'woocommerce' ),
			)
**Tags:** #filter

### woocommerce_product_reviews_list_table_prepare_items_args
**Params:** array $args
**Since:** 7.0.0 | **Tags:** #filter
Provides an opportunity to alter the comment query arguments used within the product reviews admin list table.

### woocommerce_product_reviews_page_capability
**Params:** string $capability, string $context
**Since:** 6.7.0 | **Tags:** #filter
Filters whether the current user can manage product reviews. This is aligned to {@see \wc_rest_check_product_reviews_permissions()}

### woocommerce_product_reviews_pending_count
**Params:** array $count
**Since:** 7.0.0 | **Tags:** #filter
Provides an opportunity to alter the pending comment count used within the product reviews admin list table.

### woocommerce_product_reviews_table_column_$COLUMN_NAME_content
**Tags:** #filter

### woocommerce_product_reviews_table_columns
**Params:** array $columns
**Since:** 6.7.0 | **Tags:** #filter
Filters the table columns.

### woocommerce_product_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_product_short_description_editor_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_product_single_add_to_cart_text
**Args:** __( 'Add to cart', 'woocommerce' ), $this
**Tags:** #filter

### woocommerce_product_source
**Params:** int $product_id, object $post
**Tags:** #filter
Send a Tracks event when a product is updated.

### woocommerce_product_stock_default_amount
**Params:** int $default_stock_amount
**Since:** 10.6.0 | **Tags:** #filter
Filters product default stock amount.

### woocommerce_product_stock_status_options
**Args:** array(
			ProductStockStatus::IN_STOCK     => __( 'In stock', 'woocommerce' ),
			ProductStockStatus::OUT_OF_STOCK => __( 'Out of stock', 'woocommerce' ),
			ProductStockStatus::ON_BACKORDER => __( 'On backorder', 'woocommerce' ),
		)
**Tags:** #filter

### woocommerce_product_stock_status_use_radio
**Args:** $stock_status_count <= 3 && $stock_status_count >= 1
**Tags:** #filter

### woocommerce_product_supports
**Params:** string $feature
**Since:** 2.5.0 | **Tags:** #filter
Check if a product supports a given feature. Product classes should override this to declare support (or lack of support) for a feature.

### woocommerce_product_template_csv_file_path
**Args:** $template_path, $template_name
**Tags:** #filter

### woocommerce_product_title
**Args:** $this->get_name(), $this
**Tags:** #filter

### woocommerce_product_type_query
**Params:** int $product_id
**Since:** 3.0.0 | **Tags:** #filter
Get the product type for a product.

### woocommerce_product_upsell_ids
**Args:** $this->get_upsell_ids(), $this
**Tags:** #filter

### woocommerce_product_visibility_options
**Args:** array(
								CatalogVisibility::VISIBLE => __( 'Catalog &amp; search', 'woocommerce' ),
								CatalogVisibility::CATALOG => __( 'Catalog', 'woocommerce' ),
								CatalogVisibility::SEARCH  => __( 'Search', 'woocommerce' ),
								CatalogVisibility::HIDDEN  => __( 'Hidden', 'woocommerce' ),
							)
**Tags:** #filter

### woocommerce_products_general_settings
**Args:** $settings
**Tags:** #filter

### woocommerce_quantity_input_min_admin
**Params:** string $step, WC_Product $product, string $context
**Since:** 5.8.0 | **Tags:** #filter
Filter to change the product quantity minimum in the order editor of the admin area.

### woocommerce_quantity_input_step_admin
**Params:** string $step, WC_Product $product, string $context
**Since:** 5.8.0 | **Tags:** #filter
Filter to change the product quantity stepping in the order editor of the admin area.

### woocommerce_query_for_reserved_stock
**Params:** string $query, int $product_id, int $exclude_order_id
**Since:** 4.5.0 | **Tags:** #filter
Filter: woocommerce_query_for_reserved_stock Allows to filter the query for getting reserved stock of a product.

### woocommerce_regenerate_variation_summaries_sync_threshold
**Params:** int $threshold
**Since:** 10.2.0 | **Tags:** #filter
Filters the threshold for synchronous regeneration of variation attribute summaries. If the number of variations affected by an update is below this threshold, the summaries are regenerated synchronously. Otherwise, the regeneration is scheduled asynchronously.

### woocommerce_related_products
**Args:** $related_posts, $product_id, array(
			'limit'        => $limit,
			'excluded_ids' => $exclude_ids,
		)
**Tags:** #filter

### woocommerce_report_coupons_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_coupons_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_report_low_in_stock_query_from
**Args:** $wpdb->prepare(
				"
				FROM {$wpdb->posts} as posts
				INNER JOIN {$wpdb->wc_product_meta_lookup} AS lookup ON posts.ID = lookup.product_id
				WHERE 1=1
				AND posts.post_type IN ( 'product', 'product_variation' )
				AND posts.post_status = 'publish'
				AND lookup.stock_quantity <= %d
				AND lookup.stock_quantity > %d
				",
				$stock,
				$nostock
			)
**Tags:** #filter

### woocommerce_report_most_stocked_query_from
**Args:** $wpdb->prepare(
				"
				FROM {$wpdb->posts} as posts
				INNER JOIN {$wpdb->wc_product_meta_lookup} AS lookup ON posts.ID = lookup.product_id
				WHERE 1=1
				AND posts.post_type IN ( 'product', 'product_variation' )
				AND posts.post_status = 'publish'
				AND lookup.stock_quantity > %d
				",
				$stock
			)
**Tags:** #filter

### woocommerce_report_out_of_stock_query_from
**Args:** $wpdb->prepare(
				"
				FROM {$wpdb->posts} as posts
				INNER JOIN {$wpdb->wc_product_meta_lookup} AS lookup ON posts.ID = lookup.product_id
				WHERE 1=1
				AND posts.post_type IN ( 'product', 'product_variation' )
				AND posts.post_status = 'publish'
				AND lookup.stock_quantity <= %d
				",
				$stock
			)
**Tags:** #filter

### woocommerce_report_products_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_products_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_report_sales_by_category_get_products_in_category
**Args:** $product_ids, $category_id
**Tags:** #filter

### woocommerce_report_stock_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_stock_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_report_variations_export_columns
**Params:** array $export_columns
**Since:** 10.7.0 | **Tags:** #filter
Filter to add or remove column names from the variations report for export.

### woocommerce_report_variations_prepare_export_item
**Params:** array $export_item, array $item
**Since:** 10.7.0 | **Tags:** #filter
Filter to prepare extra columns in the export item for the variations report.

### woocommerce_rest_preprocess_product_review
**Params:** array $prepared_review, WP_REST_Request $request
**Since:** 3.5.0 | **Tags:** #filter
Filters a review after it is prepared for the database. Allows modification of the review right after it is prepared for the database.

### woocommerce_sale_badge_text
**Params:** string $sale_text, \WC_Product $product
**Since:** 10.0.0 | **Tags:** #filter
Filters the product sale badge text.

### woocommerce_shortcode_product_page_force_rendering
**Params:** bool $force_rendering, int $product_id
**Since:** 8.6.0 | **Tags:** #filter
Filters whether to override read permissions for unpublished products.

### woocommerce_shortcode_product_page_invalid_statuses
**Params:** array $invalid_statuses, int $product_id
**Since:** 8.6.0 | **Tags:** #filter
Filters the list of invalid statuses for the `product_page` shortcode.

### woocommerce_should_send_low_stock_notification
**Params:** int $product_id
**Since:** 4.7.0 | **Tags:** #filter
Determine if the current product should trigger a low stock notification

### woocommerce_should_send_no_stock_notification
**Params:** int $product_id
**Since:** 4.6.0 | **Tags:** #filter
Determine if the current product should trigger a no stock notification

### woocommerce_show_invalid_variations_notice
**Params:** WC_Product $product_object
**Since:** 3.6.0 | **Tags:** #filter
Shows a notice if variations are missing prices.

### woocommerce_show_variation_price
**Args:** $variation->get_price() === '' || $this->get_variation_sale_price( 'min' ) !== $this->get_variation_sale_price( 'max' ) || $this->get_variation_regular_price( 'min' ) !== $this->get_variation_regular_price( 'max' ), $this, $variation
**Tags:** #filter

### woocommerce_single_product_carousel_options
**Args:** array(
							'rtl'            => is_rtl(),
							'animation'      => 'slide',
							'smoothHeight'   => true,
							'directionNav'   => false,
							'controlNav'     => 'thumbnails',
							'slideshow'      => false,
							'animationSpeed' => 500,
							'animationLoop'  => false, // Breaks photoswipe pagination if true.
							'allowOneSlide'  => false,
						)
**Tags:** #filter

### woocommerce_single_product_photoswipe_enabled
**Args:** get_theme_support( 'wc-product-gallery-lightbox' )
**Tags:** #filter

### woocommerce_single_product_photoswipe_options
**Args:** array(
							'shareEl'               => false,
							'closeOnScroll'         => false,
							'history'               => false,
							'hideAnimationDuration' => 0,
							'showAnimationDuration' => 0,
						)
**Tags:** #filter

### woocommerce_single_product_zoom_enabled
**Args:** get_theme_support( 'wc-product-gallery-zoom' )
**Tags:** #filter

### woocommerce_single_product_zoom_options
**Args:** array()
**Tags:** #filter

### woocommerce_stock_amount
**Params:** int|float $amount
**Since:** 2.3 | **Tags:** #filter
Filter the stock amount. If an invalid value is returned by hooks, falls back to intval( $amount ).

### woocommerce_store_api_product_quantity_$VALUE_TYPE
**Tags:** #filter

### woocommerce_structured_data_product
**Args:** $markup, $product
**Tags:** #filter

### woocommerce_structured_data_product_offer
**Args:** $markup_offer, $product
**Tags:** #filter

### woocommerce_taxonomy_args_pos_product_visibility
**Params:** array $args
**Since:** 10.5.0 | **Tags:** #filter
Filter the arguments for the POS product visibility taxonomy.

### woocommerce_taxonomy_args_product_type
**Args:** array(
					'hierarchical'      => false,
					'show_ui'           => false,
					'show_in_nav_menus' => false,
					'query_var'         => is_admin(),
					'rewrite'           => false,
					'public'            => false,
					'label'             => _x( 'Product type', 'Taxonomy name', 'woocommerce' ),
				)
**Tags:** #filter

### woocommerce_taxonomy_args_product_visibility
**Args:** array(
					'hierarchical'      => false,
					'show_ui'           => false,
					'show_in_nav_menus' => false,
					'query_var'         => is_admin(),
					'rewrite'           => false,
					'public'            => false,
					'label'             => _x( 'Product visibility', 'Taxonomy name', 'woocommerce' ),
				)
**Tags:** #filter

### woocommerce_taxonomy_objects_pos_product_visibility
**Params:** array $post_types
**Since:** 10.5.0 | **Tags:** #filter
Filter the post types that the POS product visibility taxonomy is attached to.

### woocommerce_taxonomy_objects_product_type
**Args:** array( 'product' )
**Tags:** #filter

### woocommerce_taxonomy_objects_product_visibility
**Args:** array( 'product', 'product_variation' )
**Tags:** #filter

### woocommerce_update_coupon_usage_invalid_statuses
**Params:** array $invalid_statuses
**Since:** 9.0.0 | **Tags:** #filter
Allow invalid order status filtering for updating coupon usage.

### woocommerce_variable_empty_price_html
**Args:** '', $this
**Tags:** #filter

### woocommerce_variable_price_html
**Args:** $price . $this->get_price_suffix(), $this
**Tags:** #filter

### woocommerce_variation_is_active
**Args:** true, $this
**Tags:** #filter

### woocommerce_variation_is_purchasable
**Params:** bool $purchasable, object $variation
**Since:** 3.0.0 | **Tags:** #filter
Filter to adjust if a variation is purchasable.

### woocommerce_variation_is_visible
**Params:** bool $visible, int $variation_id, int $product_id, object $variation
**Since:** 3.0.0 | **Tags:** #filter
Filter to adjust if a variation is visible.

### woocommerce_weight_units
**Params:** array $weight_units
**Since:** 10.4.0 | **Tags:** #filter
Filter the available weight units.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
