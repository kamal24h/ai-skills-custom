# WooCommerce Filters: Other

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### woocommerce_available_download_count
**Args:** '<span class="woocommerce-Count count">' . sprintf( _n( '%s download remaining', '%s downloads remaining', $download['downloads_remaining'], 'woocommerce' ), $download['downloads_remaining'] ) . '</span> ', $download
**Tags:** #filter

### woocommerce_available_download_link
**Args:** '<a href="' . esc_url( $download['download_url'] ) . '">' . $download['download_name'] . '</a>', $download
**Tags:** #filter

### woocommerce_brand_thumbnail_size
**Params:** string $size
**Since:** 9.4.0 | **Tags:** #filter
Filter the brand's thumbnail size.

### woocommerce_comment_pagination_args
**Args:** array(
							'prev_text' => is_rtl() ? '&rarr;' : '&larr;',
							'next_text' => is_rtl() ? '&larr;' : '&rarr;',
							'type'      => 'list',
						)
**Tags:** #filter

### woocommerce_no_available_payment_methods_message
**Args:** esc_html__( 'Sorry, it seems that there are no available payment methods for your location. Please contact us if you require assistance or wish to make alternate arrangements.', 'woocommerce' )
**Tags:** #filter

### woocommerce_return_to_shop_redirect
**Args:** wc_get_page_permalink( 'shop' )
**Tags:** #filter

### woocommerce_return_to_shop_text
**Params:** string $default_text
**Since:** 4.6.0 | **Tags:** #filter
Filter "Return To Shop" text.

### woocommerce_reviews_title
**Args:** $reviews_title, $count, $product
**Tags:** #filter

### woocommerce_ship_to_different_address_checked
**Args:** 'shipping' === get_option( 'woocommerce_ship_to_destination' ) ? 1 : 0
**Tags:** #filter

### woocommerce_short_description
**Args:** $product->get_short_description()
**Tags:** #filter

### woocommerce_show_page_title
**Args:** true
**Tags:** #filter

### woocommerce_terms_is_checked_default
**Args:** isset( $_POST['terms'] )
**Tags:** #filter

### post_class
**Args:** $post_classes, $class, $product->get_id()
**Tags:** #filter

### subcategory_archive_thumbnail_size
**Params:** mixed $category
**Tags:** #filter
Show subcategory thumbnails.

### woocommerce_demo_store
**Params:** string $store_notice
**Since:** 1.6.4 | **Tags:** #filter
Filter demo store notice.

### woocommerce_display_item_downloads
**Args:** $html, $item, $args
**Tags:** #filter

### woocommerce_display_item_meta
**Args:** $html, $item, $args
**Tags:** #filter

### woocommerce_form_field
**Args:** $field, $key, $args, $value
**Tags:** #filter

### woocommerce_form_field_$ARGS[type]
**Tags:** #filter

### woocommerce_form_field_args
**Args:** $args, $key, $value
**Tags:** #filter

### woocommerce_get_item_data
**Params:** array $item_data, array $cart_item
**Since:** 4.3.0 | **Tags:** #filter
Filters cart item data. Filters the variation option name for custom option slugs.

### woocommerce_get_privacy_policy_text
**Args:** $text, $type
**Tags:** #filter

### woocommerce_get_remove_url
**Args:** $cart_page_url ? wp_nonce_url( add_query_arg( 'remove_item', $cart_item_key, $cart_page_url ), 'woocommerce-cart' ) : ''
**Tags:** #filter

### woocommerce_get_star_rating_html
**Args:** $html, $rating, $count
**Tags:** #filter

### woocommerce_get_terms_and_conditions_checkbox_text
**Args:** get_option( 'woocommerce_checkout_terms_and_conditions_checkbox_text', sprintf( __( 'I have read and agree to the website %s', 'woocommerce' ), '[terms]' ) )
**Tags:** #filter

### woocommerce_get_undo_url
**Args:** $cart_page_url ? wp_nonce_url( add_query_arg( $query_args, $cart_page_url ), 'woocommerce-cart' ) : '', $cart_item_key
**Tags:** #filter

### woocommerce_post_class
**Params:** array $classes, WC_Product $product
**Since:** 3.6.2 | **Tags:** #filter
WooCommerce Post Class filter.

### woocommerce_privacy_policy_page_id
**Args:** 0 < $page_id ? absint( $page_id ) : 0
**Tags:** #filter

### woocommerce_redirect_single_search_result
**Args:** true
**Tags:** #filter

### woocommerce_review_gravatar_size
**Params:** array $comment
**Tags:** #filter
Display the review authors gravatar

### woocommerce_terms_and_conditions_page_id
**Args:** 0 < $page_id ? absint( $page_id ) : 0
**Tags:** #filter

### allow_password_reset
**Args:** true, $user_data->ID
**Tags:** #filter

### woocommerce_address_to_edit
**Args:** $address, $load_address
**Tags:** #filter

### woocommerce_disable_password_change_notification
**Args:** false
**Tags:** #filter

### woocommerce_layered_nav_any_label
**Params:** array $terms, string $taxonomy, string $query_type
**Tags:** #filter
Show dropdown layered nav.

### woocommerce_layered_nav_count
**Args:** '<span class="count">(' . absint( $count ) . ')</span>', $count, $term
**Tags:** #filter

### woocommerce_layered_nav_count_maybe_cache
**Args:** true
**Tags:** #filter

### woocommerce_layered_nav_link
**Args:** $link
**Tags:** #filter

### woocommerce_layered_nav_term_html
**Args:** $term_html, $term, $link, $count
**Tags:** #filter

### woocommerce_rating_filter_count
**Args:** "({$count})", $count, $rating
**Tags:** #filter

### woocommerce_rating_filter_link
**Args:** $link_ratings ? add_query_arg( 'rating_filter', $link_ratings, $link ) : remove_query_arg( 'rating_filter' )
**Tags:** #filter

### woocommerce_data_store_wp_$THIS->META_TYPE_read_meta
**Tags:** #filter

### woocommerce_file_download_path
**Params:** string $file, WC_Product $product, string $key
**Since:** 2.1.0 | **Tags:** #filter
Filter for the path of the downloadable file.

### woocommerce_get_wp_query_args
**Args:** $wp_query_args, $query_vars
**Tags:** #filter

### woocommerce_get_zone_criteria
**Params:** array $criteria, array $package, array $postcode_locations
**Since:** 3.6.6 | **Tags:** #filter
Get shipping zone criteria

### woocommerce_variable_children_args
**Args:** $all_args, $product, false
**Tags:** #filter

### wp_search_stopwords
**Args:** $stopwords
**Tags:** #filter

### $filter_name
**Tags:** #filter

### $name
**Tags:** #filter

### $tag
**Tags:** #filter

### ABSTRACTCONTROLLER->GET_HOOK_PREFIXcollection_params
**Tags:** #filter

### ABSTRACTCONTROLLER->GET_HOOK_PREFIXitem_response
**Tags:** #filter

### ABSTRACTCONTROLLER->GET_HOOK_PREFIXitem_schema
**Tags:** #filter

### CONTROLLER->GET_HOOK_PREFIXcollection_query_args
**Tags:** #filter

### CONTROLLER->GET_HOOK_PREFIXobject_trashable
**Tags:** #filter

### WC_BACKGROUND_PROCESS->IDENTIFIER_cron_interval
**Tags:** #filter

### WC_CUSTOMER->GET_HOOK_PREFIX$ADDRESS_TYPE_$PROP
**Tags:** #filter

### WC_CUSTOMER->GET_HOOK_PREFIX$PROP
**Tags:** #filter

### WC_DATA->GET_HOOK_PREFIX$KEY
**Tags:** #filter

### WC_DATA->GET_HOOK_PREFIX$PROP
**Tags:** #filter

### WC_ORDER->GET_HOOK_PREFIX$ADDRESS_TYPE_$PROP
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXheight
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXimage_id
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXlength
**Tags:** #filter

### WC_PRODUCT_VARIATION->GET_HOOK_PREFIXwidth
**Tags:** #filter

### WC_WCCOM_Site::AUTH_ERROR_FILTER_NAME
**Tags:** #filter

### WP_BACKGROUND_PROCESS->IDENTIFIER_cron_interval
**Tags:** #filter

### WP_BACKGROUND_PROCESS->IDENTIFIER_default_time_limit
**Tags:** #filter

### WP_BACKGROUND_PROCESS->IDENTIFIER_memory_exceeded
**Tags:** #filter

### WP_BACKGROUND_PROCESS->IDENTIFIER_queue_lock_time
**Tags:** #filter

### WP_BACKGROUND_PROCESS->IDENTIFIER_time_exceeded
**Tags:** #filter

### __experimental_woocommerce_blocks_payment_gateway_features_list
**Params:** array $features, string $name
**Since:** 4.4.0 | **Tags:** #filter
Filter to control what features are available for each payment gateway.

### __experimental_woocommerce_store_api_batch_request_methods
**Args:** array( 'POST', 'PUT', 'PATCH', 'DELETE' )
**Tags:** #filter

### comment_row_actions
**Params:** string[] $actions, WP_Comment $item
**Since:** 9.8.0 | **Tags:** #filter
Filters the action links displayed for each review in the Reviews list table.

### comment_text
**Args:** $comment_text, $comment, $args
**Tags:** #filter

### deprecated_function_trigger_error
**Params:** bool $trigger
**Since:** 7.3.0 | **Tags:** #filter
Filters whether to trigger an error for deprecated functions. (Same as WP core)

### handle_bulk_actions-$SCREEN
**Tags:** #filter

### https_local_ssl_verify
**Args:** false
**Tags:** #filter

### import_upload_size_limit
**Args:** wp_max_upload_size()
**Tags:** #filter

### is_woocommerce
**Args:** is_shop() || is_product_taxonomy() || is_product()
**Tags:** #filter

### login_errors
**Args:** $e->getMessage()
**Tags:** #filter

### plugin_locale
**Args:** determine_locale(), 'woocommerce'
**Tags:** #filter

### plugins_update_check_locales
**Params:** array $locales
**Since:** 3.7.0 | **Tags:** #filter
Filters the locales requested for plugin translations.

### postmeta_form_keys
**Params:** array|null $keys, \WC_Order $order
**Since:** 6.9.0 | **Tags:** #filter
Filters values for the meta key dropdown in the Custom Fields meta box. Compatibility filter for `postmeta_form_keys` filter.

### postmeta_form_limit
**Params:** int $limit
**Since:** 8.8.0 | **Tags:** #filter
Compatibility filter for 'postmeta_form_limit', which filters the number of custom fields to retrieve for the drop-down in the Custom Fields meta box.

### query_vars
**Args:** $wp->public_query_vars
**Tags:** #filter

### sanitize_taxonomy_name
**Params:** string $taxonomy
**Tags:** #filter
Sanitize taxonomy names. Slug format (no spaces, lowercase). Urldecode is used to reverse munging of UTF8 characters.

### self::FILTER_NAME
**Tags:** #filter

### self::FILTER_NAME_SPECS
**Tags:** #filter

### the_content
**Args:** str_replace( ']]>', ']]&gt;', $post_content )
**Tags:** #filter

### twentynineteen_custom_colors_lightness
**Args:** 33
**Tags:** #filter

### wc_batch_processing_log_message
**Params:** string $error_message, \Exception $error, BatchProcessorInterface $batch_processor, array $batch, array $error_context
**Since:** 6.8.0 | **Tags:** #filter
Filters the error message for a batch processing.

### wc_batch_processing_max_attempts
**Params:** int $failure_threshold, BatchProcessorInterface $batch_processor, array $process_details
**Since:** 9.1.0 | **Tags:** #filter
Controls the failure threshold for batch processors. That is, the number of times we'll attempt to process a batch that has resulted in a failure. Once above this threshold, the processor won't be re-scheduled and will be removed from the queue.

### wc_help_tip
**Params:** string $tip_html, string $sanitized_tip, string $tip, bool $allow_html
**Since:** 7.7.0 | **Tags:** #filter
Filter the help tip.

### wc_object_cache_get_engine
**Params:** CacheEngine $engine, ObjectCache $cache_instance
**Since:** 7.4.0 | **Tags:** #filter
Filters the underlying cache engine to be used by an instance of ObjectCache.

### wc_payment_gateway_form_saved_payment_methods_html
**Args:** $html, $this
**Tags:** #filter

### wc_privacy_policy_content
**Args:** $content
**Tags:** #filter

### wc_round_tax_total
**Args:** $rounded_tax, $value, $precision, WC_TAX_ROUNDING_MODE
**Tags:** #filter

### wc_tax_enabled
**Args:** get_option( 'woocommerce_calc_taxes' ) === 'yes'
**Tags:** #filter

### wc_tracks_use_batch_requests
**Params:** bool $use_batching
**Since:** 10.5.0 | **Tags:** #filter
Filters whether to use batch requests for tracking pixels.

### webhook_row_actions
**Args:** $actions, $webhook
**Tags:** #filter

### woo_com_base_url
**Args:** 'https://woocommerce.com/'
**Tags:** #filter

### woocommerce_$OBJECT_TYPE_data_store
**Tags:** #filter

### woocommerce_$THIS->EXPORT_TYPE_export_batch_limit
**Tags:** #filter

### woocommerce_$THIS->EXPORT_TYPE_export_column_names
**Tags:** #filter

### woocommerce_$THIS->EXPORT_TYPE_export_delimiter
**Tags:** #filter

### woocommerce_$THIS->EXPORT_TYPE_export_get_filename
**Tags:** #filter

### woocommerce_$THIS->EXPORT_TYPE_export_rows
**Tags:** #filter

### woocommerce_$TYPEfields
**Tags:** #filter

### woocommerce_add_$NOTICE_TYPE
**Tags:** #filter

### woocommerce_add_message
**Args:** $message
**Tags:** #filter

### woocommerce_add_payment_method_form_is_valid
**Args:** true
**Tags:** #filter

### woocommerce_addons_sections
**Args:** $addon_sections
**Tags:** #filter

### woocommerce_address_providers
**Params:** array $providers
**Since:** 9.9.0 | **Tags:** #filter
Filter the registered address providers.

### woocommerce_ajax_get_endpoint
**Args:** add_query_arg( 'wc-ajax', $request, remove_query_arg( array( 'remove_item', 'add-to-cart', 'added-to-cart', 'order_again', '_wpnonce' ), home_url( '/', 'relative' ) ) ), $request
**Tags:** #filter

### woocommerce_allow_marketplace_suggestions
**Args:** true
**Tags:** #filter

### woocommerce_allow_payment_recommendations
**Args:** true
**Tags:** #filter

### woocommerce_analytics_$FIELD
**Tags:** #filter

### woocommerce_analytics_$SNAKE_NAME_query_args
**Tags:** #filter

### woocommerce_analytics_$SNAKE_NAME_select_query
**Tags:** #filter

### woocommerce_analytics_$THIS->CONTEXT_query_args
**Tags:** #filter

### woocommerce_analytics_$THIS->CONTEXT_select_query
**Tags:** #filter

### woocommerce_analytics_categories_query_args
**Args:** array(
					'orderby'       => 'items_sold',
					'order'         => 'desc',
					'after'         => $after,
					'before'        => $before,
					'per_page'      => $per_page,
					'extended_info' => true,
				)
**Tags:** #filter

### woocommerce_analytics_categories_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_clauses_$TYPE
**Tags:** #filter

### woocommerce_analytics_clauses_$TYPE_$THIS->CONTEXT
**Tags:** #filter

### woocommerce_analytics_disable_action_scheduling
**Args:** false
**Tags:** #filter

### woocommerce_analytics_downloads_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_downloads_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_downloads_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_downloads_stats_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_import_interval
**Params:** int $interval
**Since:** 10.4.0 | **Tags:** #filter
Filter the analytics import interval.

### woocommerce_analytics_regenerate_batch_size
**Params:** int $batch_size, string $action
**Tags:** #filter
Filter the batch size for regenerating a report table.

### woocommerce_analytics_report_menu_items
**Args:** $report_pages
**Tags:** #filter

### woocommerce_analytics_report_schedulers
**Args:** array(
				new CustomersScheduler(),
				new OrdersScheduler(),
			)
**Tags:** #filter

### woocommerce_analytics_report_should_use_cache
**Params:** bool $use_cache, string $cache_key
**Tags:** #filter
Determines if a report will utilize caching.

### woocommerce_analytics_revenue_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_revenue_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_taxes_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_taxes_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_analytics_taxes_stats_query_args
**Args:** $this->get_query_vars()
**Tags:** #filter

### woocommerce_analytics_taxes_stats_select_query
**Args:** $results, $args
**Tags:** #filter

### woocommerce_apply_base_tax_for_local_pickup
**Args:** true
**Since:** 6.8.0 | **Tags:** #filter
Filters whether apply base tax for local pickup shipping method or not.

### woocommerce_available_payment_gateways
**Args:** $_available_gateways
**Tags:** #filter

### woocommerce_background_image_regeneration
**Params:** WP_Customize_Manager $wp_customize
**Tags:** #filter
Product images section.

### woocommerce_bacs_icon
**Args:** ''
**Tags:** #filter

### woocommerce_base_tax_rates
**Args:** self::find_rates(
				array(
					'country'   => WC()->countries->get_base_country(),
					'state'     => WC()->countries->get_base_state(),
					'postcode'  => WC()->countries->get_base_postcode(),
					'city'      => WC()->countries->get_base_city(),
					'tax_class' => $tax_class,
				)
			), $tax_class
**Tags:** #filter

### woocommerce_batch_processor_watchdog_delay_seconds
**Params:** int $delay
**Since:** 8.2.0 | **Tags:** #filter
Modify the delay interval for the batch processor's watchdog events.

### woocommerce_blocks_hook_compatibility_additional_data
**Params:** array $data, string $class_name
**Since:** 9.5.0 | **Tags:** #filter
When extensions implement their equivalent blocks of the template hook functions, they can use this filter to register their old hooked data here, so in the blockified template, the old hooked functions can be removed in favor of the new blocks while keeping the old hooked functions working in classic templates. Accepts an array of hooked data. The array should be in the following format: [ [ hook => <hook-name>, function => <function-name>, priority => <priority>, ], ... ] Where: - hook-name is the name of the hook that have the functions hooked to. - function-name is the hooked function name. - priority is the priority of the hooked function.

### woocommerce_blocks_pre_get_routes_from_namespace
**Params:** array $routes, string $namespace, string $context
**Since:** 8.7.0 | **Tags:** #filter
Gives opportunity to return routes without invoking the compute intensive REST API.

### woocommerce_blocks_register_script_dependencies
**Params:** array $dependencies, string $handle
**Since:** 3.0.0 | **Tags:** #filter
Filters the list of script dependencies.

### woocommerce_blueprint_upload_max_file_size
**Params:** int $max_size
**Since:** 9.3.0 | **Tags:** #filter
Filters the maximum allowed file size for blueprint uploads.

### woocommerce_brands_list_alphabet
**Args:** range( 'a', 'z' )
**Tags:** #filter

### woocommerce_brands_list_locale
**Args:** 'en_US.UTF-8'
**Tags:** #filter

### woocommerce_brands_list_numbers
**Args:** '0-9'
**Tags:** #filter

### woocommerce_bulk_action_ids
**Params:** string $redirect_to, string $action, array $ids
**Tags:** #filter
Handle bulk actions.

### woocommerce_calc_tax
**Args:** $taxes, $price, $rates, $price_includes_tax, $deprecated
**Tags:** #filter

### woocommerce_calculate_item_totals_taxes
**Args:** WC_Tax::calc_tax( $item->total, $item->tax_rates, $item->price_includes_tax ), $item, $this
**Tags:** #filter

### woocommerce_calculated_total
**Args:** $this->get_total( 'total' ), $this->cart
**Tags:** #filter

### woocommerce_change_term_counts
**Params:** array $valid_taxonomies
**Since:** 2.1.0 | **Tags:** #filter
Filter which product taxonomies should have their term counts overridden to take catalog visibility into account.

### woocommerce_cheque_icon
**Args:** ''
**Tags:** #filter

### woocommerce_cod_icon
**Args:** ''
**Tags:** #filter

### woocommerce_coming_soon_exclude
**Params:** bool $is_excluded
**Since:** 9.1.0 | **Tags:** #filter
Check if there is an exclusion.

### woocommerce_community_support_url
**Args:** 'https://wordpress.org/support/plugin/woocommerce/'
**Tags:** #filter

### woocommerce_continents
**Args:** include WC()->plugin_path() . '/i18n/continents.php'
**Tags:** #filter

### woocommerce_continue_shopping_redirect
**Args:** wc_get_raw_referer() ? wp_validate_redirect( wc_get_raw_referer(), false ) : wc_get_page_permalink( 'shop' )
**Tags:** #filter

### woocommerce_cookie
**Params:** string $cookie
**Since:** 3.6.0 | **Tags:** #filter
Filter the cookie name.

### woocommerce_cookie_httponly
**Args:** $httponly, $name, $value, $expire, $secure
**Tags:** #filter

### woocommerce_countries
**Args:** include WC()->plugin_path() . '/i18n/countries.php'
**Tags:** #filter

### woocommerce_countries_allowed_countries
**Params:** array $countries
**Since:** 3.3.0 | **Tags:** #filter
Filter the list of allowed selling countries.

### woocommerce_countries_allowed_country_states
**Args:** $states
**Tags:** #filter

### woocommerce_countries_base_address
**Args:** $base_address
**Tags:** #filter

### woocommerce_countries_base_address_2
**Args:** $base_address_2
**Tags:** #filter

### woocommerce_countries_base_city
**Args:** $base_city
**Tags:** #filter

### woocommerce_countries_base_country
**Args:** $default['country']
**Tags:** #filter

### woocommerce_countries_base_postcode
**Args:** $base_postcode
**Tags:** #filter

### woocommerce_countries_base_state
**Args:** $default['state']
**Tags:** #filter

### woocommerce_countries_estimated_for_prefix
**Args:** $return, $country_code
**Tags:** #filter

### woocommerce_countries_ex_tax_or_vat
**Args:** $return
**Tags:** #filter

### woocommerce_countries_inc_tax_or_vat
**Args:** $return
**Tags:** #filter

### woocommerce_countries_tax_or_vat
**Args:** $return
**Tags:** #filter

### woocommerce_countries_using_vat
**Args:** $countries
**Tags:** #filter

### woocommerce_country_locale_field_selectors
**Args:** $locale_fields
**Tags:** #filter

### woocommerce_create_page_id
**Params:** mixed $slug, string $option, string $page_title, string $page_content, int $post_parent, string $post_status
**Tags:** #filter
Create a page and store the ID in an option.

### woocommerce_create_pages
**Args:** array(
				'shop'           => array(
					'name'    => _x( 'shop', 'Page slug', 'woocommerce' ),
					'title'   => _x( 'Shop', 'Page title', 'woocommerce' ),
					'content' => '',
				),
				'cart'           => array(
					'name'    => _x( 'cart', 'Page slug', 'woocommerce' ),
					'title'   => _x( 'Cart', 'Page title', 'woocommerce' ),
					'content' => $cart_page_content,
				),
				'checkout'       => array(
					'name'    => _x( 'checkout', 'Page slug', 'woocommerce' ),
					'title'   => _x( 'Checkout', 'Page title', 'woocommerce' ),
					'content' => $checkout_page_content,
				),
				'myaccount'      => array(
					'name'    => _x( 'my-account', 'Page slug', 'woocommerce' ),
					'title'   => _x( 'My account', 'Page title', 'woocommerce' ),
					'content' => '<!-- wp:shortcode -->[' . $my_account_shortcode . ']<!-- /wp:shortcode -->',
				),
				'refund_returns' => array(
					'name'        => _x( 'refund_returns', 'Page slug', 'woocommerce' ),
					'title'       => _x( 'Refund and Returns Policy', 'Page title', 'woocommerce' ),
					'content'     => self::get_refunds_return_policy_page_content(),
					'post_status' => 'draft',
				),
			)
**Tags:** #filter

### woocommerce_credit_card_form_fields
**Args:** $default_fields, $this->id
**Tags:** #filter

### woocommerce_credit_card_type_labels
**Args:** array(
			'mastercard'       => _x( 'MasterCard', 'Name of credit card', 'woocommerce' ),
			'visa'             => _x( 'Visa', 'Name of credit card', 'woocommerce' ),
			'discover'         => _x( 'Discover', 'Name of credit card', 'woocommerce' ),
			'american express' => _x( 'American Express', 'Name of credit card', 'woocommerce' ),
			'cartes bancaires' => _x( 'Cartes Bancaires', 'Name of credit card', 'woocommerce' ),
			'diners'           => _x( 'Diners', 'Name of credit card', 'woocommerce' ),
			'jcb'              => _x( 'JCB', 'Name of credit card', 'woocommerce' ),
		)
**Tags:** #filter

### woocommerce_csv_exporter_fopen_mode
**Params:** string $fopen_mode
**Since:** 6.8.0 | **Tags:** #filter
Filters the mode parameter which specifies the type of access you require to the stream (used during file writing for CSV exports). Defaults to 'a+' (which supports both reading and writing, and places the file pointer at the end of the file).

### woocommerce_csv_import_valid_filetypes
**Params:** array $valid_filetypes
**Since:** 3.6.5 | **Tags:** #filter
Filter CSV valid file types.

### woocommerce_csv_importer_check_import_file_path
**Params:** bool $check_import_file_path, string $file
**Since:** 3.6.4 | **Tags:** #filter
Filter check for CSV file path.

### woocommerce_currencies
**Params:** array $currencies
**Since:** 2.1.0 | **Tags:** #filter
Filters the list of available currencies.

### woocommerce_currency
**Args:** get_option( 'woocommerce_currency' )
**Tags:** #filter

### woocommerce_currency_symbol
**Args:** $currency_symbol, $currency
**Tags:** #filter

### woocommerce_currency_symbols
**Args:** array(
			'AED' => '&#x62f;.&#x625;',
			'AFN' => '&#x60b;',
			'ALL' => 'L',
			'AMD' => 'AMD',
			'ANG' => '&fnof;',
			'AOA' => 'Kz',
			'ARS' => '&#36;',
			'AUD' => '&#36;',
			'AWG' => 'Afl.',
			'AZN' => '&#8380;',
			'BAM' => 'KM',
			'BBD' => '&#36;',
			'BDT' => '&#2547;&nbsp;',
			'BGN' => '&#1083;&#1074;.',
			'BHD' => '.&#x62f;.&#x628;',
			'BIF' => 'Fr',
			'BMD' => '&#36;',
			'BND' => '&#36;',
			'BOB' => 'Bs.',
			'BRL' => '&#82;&#36;',
			'BSD' => '&#36;',
			'BTC' => '&#3647;',
			'BTN' => 'Nu.',
			'BWP' => 'P',
			'BYR' => 'Br',
			'BYN' => 'Br',
			'BZD' => '&#36;',
			'CAD' => '&#36;',
			'CDF' => 'Fr',
			'CHF' => '&#67;&#72;&#70;',
			'CLP' => '&#36;',
			'CNY' => '&yen;',
			'COP' => '&#36;',
			'CRC' => '&#x20a1;',
			'CUC' => '&#36;',
			'CUP' => '&#36;',
			'CVE' => '&#36;',
			'CZK' => '&#75;&#269;',
			'DJF' => 'Fr',
			'DKK' => 'kr.',
			'DOP' => 'RD&#36;',
			'DZD' => '&#x62f;.&#x62c;',
			'EGP' => 'EGP',
			'ERN' => 'Nfk',
			'ETB' => 'Br',
			'EUR' => '&euro;',
			'FJD' => '&#36;',
			'FKP' => '&pound;',
			'GBP' => '&pound;',
			'GEL' => '&#x20be;',
			'GGP' => '&pound;',
			'GHS' => '&#x20b5;',
			'GIP' => '&pound;',
			'GMD' => 'D',
			'GNF' => 'Fr',
			'GTQ' => 'Q',
			'GYD' => '&#36;',
			'HKD' => '&#36;',
			'HNL' => 'L',
			'HRK' => 'kn',
			'HTG' => 'G',
			'HUF' => '&#70;&#116;',
			'IDR' => 'Rp',
			'ILS' => '&#8362;',
			'IMP' => '&pound;',
			'INR' => '&#8377;',
			'IQD' => '&#x62f;.&#x639;',
			'IRR' => '&#xfdfc;',
			'IRT' => '&#x062A;&#x0648;&#x0645;&#x0627;&#x0646;',
			'ISK' => 'kr.',
			'JEP' => '&pound;',
			'JMD' => '&#36;',
			'JOD' => '&#x62f;.&#x627;',
			'JPY' => '&yen;',
			'KES' => 'KSh',
			'KGS' => '&#x441;&#x43e;&#x43c;',
			'KHR' => '&#x17db;',
			'KMF' => 'Fr',
			'KPW' => '&#x20a9;',
			'KRW' => '&#8361;',
			'KWD' => '&#x62f;.&#x643;',
			'KYD' => '&#36;',
			'KZT' => '&#8376;',
			'LAK' => '&#8365;',
			'LBP' => '&#x644;.&#x644;',
			'LKR' => '&#xdbb;&#xdd4;',
			'LRD' => '&#36;',
			'LSL' => 'L',
			'LYD' => '&#x62f;.&#x644;',
			'MAD' => '&#x62f;.&#x645;.',
			'MDL' => 'MDL',
			'MGA' => 'Ar',
			'MKD' => '&#x434;&#x435;&#x43d;',
			'MMK' => 'Ks',
			'MNT' => '&#x20ae;',
			'MOP' => 'P',
			'MRU' => 'UM',
			'MUR' => '&#x20a8;',
			'MVR' => '.&#x783;',
			'MWK' => 'MK',
			'MXN' => '&#36;',
			'MYR' => '&#82;&#77;',
			'MZN' => 'MT',
			'NAD' => 'N&#36;',
			'NGN' => '&#8358;',
			'NIO' => 'C&#36;',
			'NOK' => '&#107;&#114;',
			'NPR' => '&#8360;',
			'NZD' => '&#36;',
			'OMR' => '&#x631;.&#x639;.',
			'PAB' => 'B/.',
			'PEN' => 'S/',
			'PGK' => 'K',
			'PHP' => '&#8369;',
			'PKR' => '&#8360;',
			'PLN' => '&#122;&#322;',
			'PRB' => '&#x440;.',
			'PYG' => '&#8370;',
			'QAR' => '&#x631;.&#x642;',
			'RMB' => '&yen;',
			'RON' => 'lei',
			'RSD' => '&#1088;&#1089;&#1076;',
			'RUB' => '&#8381;',
			'RWF' => 'Fr',
			'SAR' => '&#x631;.&#x633;',
			'SBD' => '&#36;',
			'SCR' => '&#x20a8;',
			'SDG' => '&#x62c;.&#x633;.',
			'SEK' => '&#107;&#114;',
			'SGD' => '&#36;',
			'SHP' => '&pound;',
			'SLL' => 'Le',
			'SOS' => 'Sh',
			'SRD' => '&#36;',
			'SSP' => '&pound;',
			'STN' => 'Db',
			'SYP' => '&#x644;.&#x633;',
			'SZL' => 'E',
			'THB' => '&#3647;',
			'TJS' => '&#x405;&#x41c;',
			'TMT' => 'm',
			'TND' => '&#x62f;.&#x62a;',
			'TOP' => 'T&#36;',
			'TRY' => '&#8378;',
			'TTD' => '&#36;',
			'TWD' => '&#78;&#84;&#36;',
			'TZS' => 'Sh',
			'UAH' => '&#8372;',
			'UGX' => 'UGX',
			'USD' => '&#36;',
			'UYU' => '&#36;',
			'UZS' => 'UZS',
			'VEF' => 'Bs F',
			'VES' => 'Bs.',
			'VND' => '&#8363;',
			'VUV' => 'Vt',
			'WST' => 'T',
			'XAF' => 'CFA',
			'XCD' => '&#36;',
			'XOF' => 'CFA',
			'XPF' => 'XPF',
			'YER' => '&#xfdfc;',
			'ZAR' => '&#82;',
			'ZMW' => 'ZK',
		)
**Tags:** #filter

### woocommerce_custom_nav_menu_items
**Args:** $endpoints
**Tags:** #filter

### woocommerce_data_stores
**Args:** $this->stores
**Tags:** #filter

### woocommerce_database_max_index_length
**Params:** int $max_index_length
**Since:** 8.0.0 | **Tags:** #filter
Filters the maximum index length in the database. Indexes have a maximum size of 767 bytes. Historically, we haven't need to be concerned about that. As of WP 4.2, however, they moved to utf8mb4, which uses 4 bytes per character. This means that an index which used to have room for floor(767/3) = 255 characters, now only has room for floor(767/4) = 191 characters. Additionally, MyISAM engine also limits the index size to 1000 bytes. We add this filter so that interested folks on InnoDB engine can increase the size till allowed 3071 bytes.

### woocommerce_database_tables
**Args:** array(
					'woocommerce_sessions',
					'woocommerce_api_keys',
					'woocommerce_attribute_taxonomies',
					'woocommerce_downloadable_product_permissions',
					'woocommerce_order_items',
					'woocommerce_order_itemmeta',
					'woocommerce_tax_rates',
					'woocommerce_tax_rate_locations',
					'woocommerce_shipping_zones',
					'woocommerce_shipping_zone_locations',
					'woocommerce_shipping_zone_methods',
					'woocommerce_payment_tokens',
					'woocommerce_payment_tokenmeta',
					'woocommerce_log',
				)
**Tags:** #filter

### woocommerce_date_format
**Args:** $date_format
**Tags:** #filter

### woocommerce_date_input_html_pattern
**Params:** string $pattern
**Tags:** #filter
Hook to customize the regular expression that validates dates entered in the WooCommerce admin editors.

### woocommerce_db_update_schedule_delay
**Params:** int $delay
**Since:** 9.9.0 | **Tags:** #filter
Filters the delay in seconds to apply to the scheduling of database updates when automatic updates are enabled.

### woocommerce_debug_tools
**Args:** $tools
**Tags:** #filter

### woocommerce_default_address_fields
**Args:** $fields
**Tags:** #filter

### woocommerce_delete_expired_transient_files_interval
**Params:** int $interval
**Since:** 8.5.0 | **Tags:** #filter
Filter to alter the interval between the actions that delete expired transient files.

### woocommerce_delete_version_transients_limit
**Args:** 1000
**Tags:** #filter

### woocommerce_disable_compatibility_layer
**Params:** boolean $is_disabled_compatibility_layer
**Since:** 7.6.0 | **Tags:** #filter
Filter to disable the compatibility layer for the blockified templates. This hook allows to disable the compatibility layer for the blockified.

### woocommerce_display_update_footer_text
**Args:** in_array( $current_screen->id, $wc_pages, true )
**Tags:** #filter

### woocommerce_docs_url
**Args:** 'https://woocommerce.com/documentation/plugins/woocommerce/'
**Tags:** #filter

### woocommerce_echeck_form_fields
**Args:** $default_fields, $this->id
**Tags:** #filter

### woocommerce_edit_address_slugs
**Params:** string $id, bool $flip
**Tags:** #filter
Get the edit address slug translation.

### woocommerce_enable_auto_update_db
**Args:** true
**Tags:** #filter

### woocommerce_enable_deprecated_additional_flat_rates
**Args:** $this->get_option( 'options', false )
**Tags:** #filter

### woocommerce_enable_hpos_by_default_for_new_shops
**Args:** true
**Tags:** #filter

### woocommerce_enable_post_clause_filtering
**Params:** bool $is_main_query, WP_Query $wp_query
**Since:** 9.9.0 | **Tags:** #filter
Filter whether to add the filter post clauses

### woocommerce_enable_setup_wizard
**Args:** true
**Tags:** #filter

### woocommerce_endpoint_$ENDPOINT_title
**Tags:** #filter

### woocommerce_enqueue_styles
**Args:** array(
				'woocommerce-layout'      => array(
					'src'     => self::get_asset_url( 'assets/css/woocommerce-layout.css' ),
					'deps'    => '',
					'version' => $version,
					'media'   => 'all',
					'has_rtl' => true,
				),
				'woocommerce-smallscreen' => array(
					'src'     => self::get_asset_url( 'assets/css/woocommerce-smallscreen.css' ),
					'deps'    => 'woocommerce-layout',
					'version' => $version,
					'media'   => 'only screen and (max-width: ' . apply_filters( 'woocommerce_style_smallscreen_breakpoint', '768px' ) . ')',
					'has_rtl' => true,
				),
				'woocommerce-general'     => array(
					'src'     => self::get_asset_url( 'assets/css/woocommerce.css' ),
					'deps'    => '',
					'version' => $version,
					'media'   => 'all',
					'has_rtl' => true,
				),
			)
**Tags:** #filter

### woocommerce_european_union_countries
**Args:** $countries, $type
**Tags:** #filter

### woocommerce_explat_request_args
**Args:** $args
**Tags:** #filter

### woocommerce_export_$THIS->EXPORT_TYPE_column_$COLUMN_NAME
**Tags:** #filter

### woocommerce_export_$THIS->EXPORT_TYPE_row_data
**Tags:** #filter

### woocommerce_export_get_ajax_query_args
**Args:** array(
				'nonce'    => wp_create_nonce( 'product-csv' ),
				'action'   => 'download_product_csv',
				'filename' => $exporter->get_filename(),
			)
**Tags:** #filter

### woocommerce_export_report_controller_map
**Params:** array $controller_map
**Since:** 9.8.0 | **Tags:** #filter
Used to add custom report controllers.

### woocommerce_export_report_data_endpoint
**Params:** string $endpoint, string $type
**Tags:** #filter
Used to add/overwrite report data endpoint.

### woocommerce_feature_description_tip
**Params:** string $desc_tip, string $feature_id, bool $disabled
**Since:** 7.1.0 | **Tags:** #filter
Filter to customize the description tip that appears under the description of each feature in the features settings page.

### woocommerce_feature_setting
**Params:** array $feature_setting, string $feature_id
**Since:** 8.0.0 | **Tags:** #filter
Allows to modify feature setting that will be used to render in the feature page.

### woocommerce_file_download_filename
**Args:** $filename, $product_id
**Tags:** #filter

### woocommerce_file_download_method
**Params:** string $method, int $product_id, string $file_path
**Since:** 4.5.0 | **Tags:** #filter
Filter download method.

### woocommerce_filter_downloads_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_find_rates
**Args:** $matched_tax_rates, $args
**Tags:** #filter

### woocommerce_format_content
**Args:** apply_filters( 'woocommerce_short_description', $raw_string ), $raw_string
**Tags:** #filter

### woocommerce_format_localized_decimal
**Args:** str_replace( '.', $decimal, strval( $value ) ), $value
**Tags:** #filter

### woocommerce_format_log_entry
**Params:** string $entry, array $args
**Since:** 3.0.0 | **Tags:** #filter
Filter the formatted log entry before it is written.

### woocommerce_format_postcode
**Args:** trim( $postcode ), $country
**Tags:** #filter

### woocommerce_formatted_address_force_country_display
**Args:** false
**Tags:** #filter

### woocommerce_formatted_address_replacements
**Args:** array(
					'{first_name}'       => $args['first_name'],
					'{last_name}'        => $args['last_name'],
					'{name}'             => sprintf(
						/* translators: 1: first name 2: last name */
						_x( '%1$s %2$s', 'full name', 'woocommerce' ),
						$args['first_name'],
						$args['last_name']
					),
					'{company}'          => $args['company'],
					'{address_1}'        => $args['address_1'],
					'{address_2}'        => $args['address_2'],
					'{city}'             => $args['city'],
					'{state}'            => $full_state,
					'{postcode}'         => $args['postcode'],
					'{country}'          => $full_country,
					'{first_name_upper}' => wc_strtoupper( $args['first_name'] ),
					'{last_name_upper}'  => wc_strtoupper( $args['last_name'] ),
					'{name_upper}'       => wc_strtoupper(
						sprintf(
							/* translators: 1: first name 2: last name */
							_x( '%1$s %2$s', 'full name', 'woocommerce' ),
							$args['first_name'],
							$args['last_name']
						)
					),
					'{company_upper}'    => wc_strtoupper( $args['company'] ),
					'{address_1_upper}'  => wc_strtoupper( $args['address_1'] ),
					'{address_2_upper}'  => wc_strtoupper( $args['address_2'] ),
					'{city_upper}'       => wc_strtoupper( $args['city'] ),
					'{state_upper}'      => wc_strtoupper( $full_state ),
					'{state_code}'       => wc_strtoupper( $state ),
					'{postcode_upper}'   => wc_strtoupper( $args['postcode'] ),
					'{country_upper}'    => wc_strtoupper( $full_country ),
				), $args
**Tags:** #filter

### woocommerce_fulfillment_before_create
**Args:** $data
**Tags:** #filter

### woocommerce_fulfillment_before_delete
**Args:** $data
**Tags:** #filter

### woocommerce_fulfillment_before_fulfill
**Params:** Fulfillment $data
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify the fulfillment data before it is fulfilled.

### woocommerce_fulfillment_before_update
**Params:** Fulfillment $data
**Since:** 10.1.0 | **Tags:** #filter
Filter to modify the fulfillment data before it is updated.

### woocommerce_fulfillment_fulfillment_statuses
**Params:** array $fulfillment_statuses
**Since:** 10.1.0 | **Tags:** #filter
This filter allows plugins to modify the list of fulfillment statuses. It can be used to add, remove, or change the fulfillment statuses available in the WooCommerce Fulfillments system.

### woocommerce_fulfillment_meta_key_translations
**Args:** array(
				'fulfillment_status' => __( 'Fulfillment Status', 'woocommerce' ),
				'shipment_tracking'  => __( 'Shipment Tracking', 'woocommerce' ),
				'shipment_provider'  => __( 'Shipment Provider', 'woocommerce' ),
			)
**Tags:** #filter

### woocommerce_fulfillment_translate_meta_key
**Args:** $field->key
**Tags:** #filter

### woocommerce_gateway_description
**Params:** string $description, string $id
**Since:** 1.5.8 | **Tags:** #filter
Filters the gateway description. Descriptions can be overridden by extending this method or through the use of `woocommerce_gateway_description` To avoid breaking custom HTML that may be returned we cannot enforce KSES at render time, so we run it here.

### woocommerce_gateway_icon
**Params:** string $icon, string $id
**Since:** 1.5.8 | **Tags:** #filter
Filter the gateway icon.

### woocommerce_gateway_method_description
**Params:** string $description, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the method description.

### woocommerce_gateway_method_title
**Params:** string $title, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the method title.

### woocommerce_gateway_title
**Params:** string $title, string $id
**Since:** 1.5.8 | **Tags:** #filter
Filter the gateway title.

### woocommerce_generate_$TYPE_html
**Tags:** #filter

### woocommerce_geolocate_ip
**Params:** string $geolocation, string $ip_address, bool $fallback, bool $api_fallback
**Since:** 3.9.0 | **Tags:** #filter
Filter to allow custom geolocation of the IP address.

### woocommerce_geolocation_ajax_get_location_hash
**Params:** string $location_hash, array $location, WC_Customer $customer
**Since:** 3.6.0 | **Tags:** #filter
Controls the location hash used in geolocation-based caching.

### woocommerce_geolocation_geoip_apis
**Args:** self::$geoip_apis
**Tags:** #filter

### woocommerce_geolocation_geoip_response_$SERVICE_NAME
**Tags:** #filter

### woocommerce_geolocation_ip_lookup_api_response
**Args:** wc_clean( $response['body'] ), $service_name
**Tags:** #filter

### woocommerce_geolocation_ip_lookup_apis
**Args:** self::$ip_lookup_apis
**Tags:** #filter

### woocommerce_geolocation_local_database_path
**Params:** string $database_path, int $version
**Tags:** #filter
Filter the geolocation database storage path.

### woocommerce_get_$PAGE_page_id
**Tags:** #filter

### woocommerce_get_$PAGE_page_permalink
**Tags:** #filter

### woocommerce_get_asset_url
**Params:** string $path
**Tags:** #filter
Return asset URL.

### woocommerce_get_availability
**Args:** array(
				'availability' => $this->get_availability_text(),
				'class'        => $this->get_availability_class(),
			), $this
**Tags:** #filter

### woocommerce_get_availability_class
**Args:** $class, $this
**Tags:** #filter

### woocommerce_get_availability_text
**Args:** $availability, $this
**Tags:** #filter

### woocommerce_get_bacs_locale
**Args:** array(
					'AU' => array(
						'sortcode' => array(
							'label' => __( 'BSB', 'woocommerce' ),
						),
					),
					'CA' => array(
						'sortcode' => array(
							'label' => __( 'Bank transit number', 'woocommerce' ),
						),
					),
					'IN' => array(
						'sortcode' => array(
							'label' => __( 'IFSC', 'woocommerce' ),
						),
					),
					'IT' => array(
						'sortcode' => array(
							'label' => __( 'Branch sort', 'woocommerce' ),
						),
					),
					'NZ' => array(
						'sortcode' => array(
							'label' => __( 'Bank code', 'woocommerce' ),
						),
					),
					'SE' => array(
						'sortcode' => array(
							'label' => __( 'Bank code', 'woocommerce' ),
						),
					),
					'US' => array(
						'sortcode' => array(
							'label' => __( 'Routing number', 'woocommerce' ),
						),
					),
					'ZA' => array(
						'sortcode' => array(
							'label' => __( 'Branch code', 'woocommerce' ),
						),
					),
				)
**Tags:** #filter

### woocommerce_get_base_location
**Args:** get_option( 'woocommerce_default_country', 'US:CA' )
**Tags:** #filter

### woocommerce_get_batch_processor
**Params:** object|null $processor, string $processor_class_name
**Since:** 6.8.0. | **Tags:** #filter
Filters the instance of a processor for a given class name.

### woocommerce_get_block_types
**Params:** array $block_types
**Since:** 9.0.0 | **Tags:** #filter
Filters the list of allowed block types.

### woocommerce_get_children
**Args:** $this->children, $this, false
**Tags:** #filter

### woocommerce_get_country_locale
**Args:** array(
					'AE' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'required' => false,
						),
					),
					'AF' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'AL' => array(
						'state' => array(
							'label' => __( 'County', 'woocommerce' ),
						),
					),
					'AO' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'AT' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'AU' => array(
						'city'     => array(
							'label' => __( 'Suburb', 'woocommerce' ),
						),
						'postcode' => array(
							'label' => __( 'Postcode', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'State', 'woocommerce' ),
						),
					),
					'AX' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'BA' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'label'    => __( 'Canton', 'woocommerce' ),
							'required' => false,
							'hidden'   => true,
						),
					),
					'BD' => array(
						'postcode' => array(
							'required' => false,
						),
						'state'    => array(
							'label' => __( 'District', 'woocommerce' ),
						),
					),
					'BE' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'BG' => array(
						'state' => array(
							'required' => false,
						),
					),
					'BH' => array(
						'postcode' => array(
							'required' => false,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'BI' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'BO' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'BS' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'BW' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
							'label'    => __( 'District', 'woocommerce' ),
						),
					),
					'BZ' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'required' => false,
						),
					),
					'CA' => array(
						'postcode' => array(
							'label' => __( 'Postal code', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'CH' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'label'    => __( 'Canton', 'woocommerce' ),
							'required' => false,
						),
					),
					'CL' => array(
						'city'     => array(
							'required' => true,
						),
						'postcode' => array(
							'required' => false,
							// Hidden for stores within Chile. @see https://github.com/woocommerce/woocommerce/issues/36546.
							'hidden'   => 'CL' === $this->get_base_country(),
						),
						'state'    => array(
							'label' => __( 'Region', 'woocommerce' ),
						),
					),
					'CN' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'CO' => array(
						'postcode' => array(
							'required' => false,
						),
						'state'    => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'CR' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'CW' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'required' => false,
						),
					),
					'CY' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'CZ' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'DE' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
						),
					),
					'DK' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'DO' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'EC' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'EE' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'ET' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'FI' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'FR' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'GG' => array(
						'state' => array(
							'required' => false,
							'label'    => __( 'Parish', 'woocommerce' ),
						),
					),
					'GH' => array(
						'postcode' => array(
							'required' => false,
						),
						'state'    => array(
							'label' => __( 'Region', 'woocommerce' ),
						),
					),
					'GP' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'GF' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'GR' => array(
						'state' => array(
							'required' => false,
						),
					),
					'GT' => array(
						'postcode' => array(
							'required' => false,
						),
						'state'    => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'HK' => array(
						'postcode' => array(
							'required' => false,
						),
						'city'     => array(
							'label' => __( 'Town / District', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'Region', 'woocommerce' ),
						),
					),
					'HN' => array(
						'state' => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'HU' => array(
						'last_name'  => array(
							'class'    => array( 'form-row-first' ),
							'priority' => 10,
						),
						'first_name' => array(
							'class'    => array( 'form-row-last' ),
							'priority' => 20,
						),
						'postcode'   => array(
							'class'    => array( 'form-row-first', 'address-field' ),
							'priority' => 65,
						),
						'city'       => array(
							'class' => array( 'form-row-last', 'address-field' ),
						),
						'address_1'  => array(
							'priority' => 71,
						),
						'address_2'  => array(
							'priority' => 72,
						),
						'state'      => array(
							'label'    => __( 'County', 'woocommerce' ),
							'required' => false,
						),
					),
					'ID' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'IE' => array(
						'postcode' => array(
							'required' => true,
							'label'    => __( 'Eircode', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'County', 'woocommerce' ),
						),
					),
					'IS' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'IL' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'IM' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'IN' => array(
						'postcode' => array(
							'label' => __( 'PIN Code', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'State', 'woocommerce' ),
						),
					),
					'IR' => array(
						'state'     => array(
							'priority' => 50,
						),
						'city'      => array(
							'priority' => 60,
						),
						'address_1' => array(
							'priority' => 70,
						),
						'address_2' => array(
							'priority' => 80,
						),
					),
					'IT' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => true,
							'label'    => __( 'Province', 'woocommerce' ),
						),
					),
					'JM' => array(
						'city'     => array(
							'label' => __( 'Town / City / Post Office', 'woocommerce' ),
						),
						'postcode' => array(
							'required' => false,
							'label'    => __( 'Postal Code', 'woocommerce' ),
						),
						'state'    => array(
							'required' => true,
							'label'    => __( 'Parish', 'woocommerce' ),
						),
					),
					'JP' => array(
						'last_name'  => array(
							'class'    => array( 'form-row-first' ),
							'priority' => 10,
						),
						'first_name' => array(
							'class'    => array( 'form-row-last' ),
							'priority' => 20,
						),
						'postcode'   => array(
							'class'    => array( 'form-row-first', 'address-field' ),
							'priority' => 65,
						),
						'state'      => array(
							'label'    => __( 'Prefecture', 'woocommerce' ),
							'class'    => array( 'form-row-last', 'address-field' ),
							'priority' => 66,
						),
						'city'       => array(
							'priority' => 67,
						),
						'address_1'  => array(
							'priority' => 68,
						),
						'address_2'  => array(
							'priority' => 69,
						),
					),
					'KN' => array(
						'postcode' => array(
							'required' => false,
							'label'    => __( 'Postal code', 'woocommerce' ),
						),
						'state'    => array(
							'required' => true,
							'label'    => __( 'Parish', 'woocommerce' ),
						),
					),
					'KR' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'KW' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'LV' => array(
						'state' => array(
							'label'    => __( 'Municipality', 'woocommerce' ),
							'required' => false,
						),
					),
					'LB' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'MF' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'MQ' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'MT' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'MZ' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'NI' => array(
						'state' => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'NL' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'NG' => array(
						'postcode' => array(
							'label'    => __( 'Postcode', 'woocommerce' ),
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'label' => __( 'State', 'woocommerce' ),
						),
					),
					'NZ' => array(
						'postcode' => array(
							'label' => __( 'Postcode', 'woocommerce' ),
						),
						'state'    => array(
							'required' => false,
							'label'    => __( 'Region', 'woocommerce' ),
						),
					),
					'NO' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'NP' => array(
						'state'    => array(
							'label' => __( 'State / Zone', 'woocommerce' ),
						),
						'postcode' => array(
							'required' => false,
						),
					),
					'PA' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'PL' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'PR' => array(
						'city'  => array(
							'label' => __( 'Municipality', 'woocommerce' ),
						),
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'PT' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'PY' => array(
						'state' => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'RE' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'RO' => array(
						'state' => array(
							'label'    => __( 'County', 'woocommerce' ),
							'required' => true,
						),
					),
					'RS' => array(
						'city'     => array(
							'required' => true,
						),
						'postcode' => array(
							'required' => true,
						),
						'state'    => array(
							'label'    => __( 'District', 'woocommerce' ),
							'required' => false,
						),
					),
					'RW' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'SG' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
						'city'  => array(
							'required' => false,
						),
					),
					'SK' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'SI' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'SR' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'SV' => array(
						'state' => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'ES' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'LI' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'LK' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'LU' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'MD' => array(
						'state' => array(
							'label' => __( 'Municipality / District', 'woocommerce' ),
						),
					),
					'SE' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'TR' => array(
						'postcode' => array(
							'priority' => 65,
						),
						'state'    => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'UG' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'city'     => array(
							'label'    => __( 'Town / Village', 'woocommerce' ),
							'required' => true,
						),
						'state'    => array(
							'label'    => __( 'District', 'woocommerce' ),
							'required' => true,
						),
					),
					'US' => array(
						'postcode' => array(
							'label' => __( 'ZIP Code', 'woocommerce' ),
						),
						'state'    => array(
							'label' => __( 'State', 'woocommerce' ),
						),
					),
					'UY' => array(
						'state' => array(
							'label' => __( 'Department', 'woocommerce' ),
						),
					),
					'GB' => array(
						'postcode' => array(
							'label' => __( 'Postcode', 'woocommerce' ),
						),
						'state'    => array(
							'label'    => __( 'County', 'woocommerce' ),
							'required' => false,
						),
					),
					'ST' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
						'state'    => array(
							'label' => __( 'District', 'woocommerce' ),
						),
					),
					'VN' => array(
						'state'     => array(
							'required' => false,
							'hidden'   => true,
						),
						'postcode'  => array(
							'priority' => 65,
							'required' => false,
							'hidden'   => false,
						),
						'address_2' => array(
							'required' => false,
							'hidden'   => false,
						),
					),
					'WS' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'YT' => array(
						'state' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
					'ZA' => array(
						'state' => array(
							'label' => __( 'Province', 'woocommerce' ),
						),
					),
					'ZW' => array(
						'postcode' => array(
							'required' => false,
							'hidden'   => true,
						),
					),
				)
**Tags:** #filter

### woocommerce_get_country_locale_base
**Args:** $this->locale['default']
**Tags:** #filter

### woocommerce_get_country_locale_default
**Args:** $this->get_default_address_fields()
**Tags:** #filter

### woocommerce_get_credit_card_type_label
**Args:** ( array_key_exists( $type, $labels ) ? $labels[ $type ] : ucwords( $type ) )
**Tags:** #filter

### woocommerce_get_default_value_for_$KEY
**Tags:** #filter

### woocommerce_get_default_value_for_$MISSING_FIELD
**Tags:** #filter

### woocommerce_get_endpoint_url
**Args:** $url, $endpoint, $value, $permalink
**Tags:** #filter

### woocommerce_get_geolocation
**Params:** array $geolocation, string $ip_address
**Since:** 3.9.0 | **Tags:** #filter
Get geolocation filter.

### woocommerce_get_image_size_$IMAGE_SIZE
**Tags:** #filter

### woocommerce_get_item_count
**Args:** $count, $item_type, $this
**Tags:** #filter

### woocommerce_get_item_downloads
**Params:** array $files, WC_Order_Item_Product $item, WC_Order $order
**Since:** 2.7.0 | **Tags:** #filter
Filters the list of downloadable files for an order item.

### woocommerce_get_items_key
**Args:** '', $item
**Tags:** #filter

### woocommerce_get_note_from_db
**Params:** Note $note
**Since:** 6.9.0 | **Tags:** #filter
Filter the note from db. This is used to modify the note before it is returned.

### woocommerce_get_path_define_tokens
**Args:** $path_tokens
**Tags:** #filter

### woocommerce_get_plugins_for_woocommerce
**Args:** $matches, $plugins
**Tags:** #filter

### woocommerce_get_plugins_with_header
**Args:** $matches, $header, $plugins
**Tags:** #filter

### woocommerce_get_query_vars
**Args:** $this->query_vars
**Tags:** #filter

### woocommerce_get_return_url
**Params:** string $return_url, WC_Order|null $order
**Since:** 2.4.0 | **Tags:** #filter
Filter the return url.

### woocommerce_get_script_data
**Args:** $params, $handle
**Tags:** #filter

### woocommerce_get_sections_$THIS->ID
**Tags:** #filter

### woocommerce_get_tax_location
**Args:** $location, $tax_class, $customer
**Tags:** #filter

### woocommerce_get_transaction_url
**Params:** string $return_url, WC_Order|null $order
**Since:** 2.2.0 | **Tags:** #filter
Filter the transaction url.

### woocommerce_helper_api_base
**Args:** 'https://woocommerce.com/wp-json/helper/1.0'
**Tags:** #filter

### woocommerce_helper_api_request_args
**Args:** $args, $endpoint
**Tags:** #filter

### woocommerce_hide_base_tables_missing_nag
**Tags:** #filter

### woocommerce_hide_download_directories_sync_complete
**Tags:** #filter

### woocommerce_hide_redirect_method_nag
**Tags:** #filter

### woocommerce_hooked_blocks_pattern_exclude_list
**Args:** array_unique( array_merge( isset( $this->hooked_block_excluded_patterns ) ? $this->hooked_block_excluded_patterns : array(), array( 'twentytwentytwo/header-centered-logo', 'twentytwentytwo/header-stacked' ) ) )
**Tags:** #filter

### woocommerce_hooked_blocks_theme_include_list
**Args:** array( 'Twenty Twenty-Four', 'Twenty Twenty-Three', 'Twenty Twenty-Two', 'Tsubaki', 'Zaino', 'Thriving Artist', 'Amulet', 'Tazza' )
**Tags:** #filter

### woocommerce_hpos_enable_sync_on_read
**Params:** bool $sync_on_read_enabled
**Since:** 8.1.0 | **Tags:** #filter
Filters whether to sync order data from posts on read. Defaults to false because sync-on-read can be dangerous when HPOS is authoritative and running correctly, as it allows the posts data store to override HPOS data.

### woocommerce_hpos_generate_join_for_search_filter
**Params:** string $join, string $search_term, string $search_filter, OrdersTableQuery $query
**Since:** 8.9.0 | **Tags:** #filter
Filter to support adding a custom order search filter. Provide a JOIN clause for a new search filter. This should be used along with `woocommerce_hpos_admin_search_filters` to declare a new custom filter, and `woocommerce_hpos_generate_where_for_search_filter` to generate the WHERE clause. Hardcoded JOINS (products) cannot be modified using this filter for consistency.

### woocommerce_hpos_generate_where_for_search_filter
**Params:** string $where, string $search_term, string $search_filter, OrdersTableQuery $query
**Since:** 8.9.0 | **Tags:** #filter
Filter to support adding a custom order search filter. Provide a WHERE clause for a custom search filter via this filter. This should be used with the `woocommerce_hpos_admin_search_filters` to declare a new custom filter, and optionally also with the `woocommerce_hpos_generate_join_for_search_filter` filter if a join is also needed. Hardcoded filters (products, customers, ID and email) cannot be modified using this filter for consistency.

### woocommerce_hpos_pre_query
**Params:** array|null $order_data, OrdersTableQuery $query, string $sql
**Since:** 8.2.0 | **Tags:** #filter
Filters the orders array before the query takes place. Return a non-null value to bypass the HPOS default order queries. If the query includes limits via the `limit`, `page`, or `offset` arguments, we encourage the `found_orders` and `max_num_pages` properties to also be set.

### woocommerce_hydration_dispatch_request
**Params:** mixed $hydration_result, WP_REST_Request $request, string $path, array $handler
**Since:** 8.9.0 | **Tags:** #filter
Similar to WP core's `rest_dispatch_request` filter, this allows plugin to override hydrating the request. Allows backward compatibility with the `rest_dispatch_request` filter by providing the same arguments.

### woocommerce_hydration_request_after_callbacks
**Params:** WP_REST_Response|WP_HTTP_Response|WP_Error|mixed $response, array $handler, WP_REST_Request $request
**Since:** 8.9.0 | **Tags:** #filter
Similar to WP core's `rest_request_after_callbacks` filter, this allows to modify the response after it has been generated. Allows backward compatibility with the `rest_request_after_callbacks` filter by providing the same arguments.

### woocommerce_image_sizes_to_resize
**Params:** array $data, int $attachment_id, string $size
**Tags:** #filter
If an intermediate size meta differs from the actual image size (settings were changed?) return false so the wrong size is not used.

### woocommerce_in_plugin_update_message
**Args:** $this->upgrade_notice ? '</p>' . wp_kses_post( $this->upgrade_notice ) . '<p class="dummy">' : ''
**Tags:** #filter

### woocommerce_install_get_tables
**Params:** array $tables
**Since:** 3.4.0 | **Tags:** #filter
Filter the list of known WooCommerce tables. If WooCommerce plugins need to add new tables, they can inject them here.

### woocommerce_install_skip_create_files
**Args:** false
**Tags:** #filter

### woocommerce_integration_description
**Args:** $this->method_description, $this
**Tags:** #filter

### woocommerce_integration_title
**Args:** $this->method_title, $this
**Tags:** #filter

### woocommerce_integrations
**Args:** $load_integrations
**Tags:** #filter

### woocommerce_internal_rounding_precision
**Params:** int $precision
**Since:** 8.8.0 | **Tags:** #filter
Filter the rounding precision for internal WC calculations. This is different from the number of decimals used for display. Generally, this filter can be used to decrease the precision, but if you choose to decrease, there maybe side effects such as off by one rounding errors for certain tax rate combinations.

### woocommerce_is_extension_store_page
**Params:** bool $is_store_page, string $url
**Since:** 9.3.0 | **Tags:** #filter
Filter if a URL is a store page.

### woocommerce_is_filtered
**Args:** ( count( WC_Query::get_layered_nav_chosen_attributes() ) > 0 || isset( $_GET['max_price'] ) || isset( $_GET['min_price'] ) || isset( $_GET['rating_filter'] ) )
**Tags:** #filter

### woocommerce_is_purchasable
**Params:** bool $purchasable, WC_Product $product
**Since:** 2.7.0 | **Tags:** #filter
Filters whether a product is purchasable.

### woocommerce_is_sold_individually
**Args:** true === $this->get_sold_individually(), $this
**Tags:** #filter

### woocommerce_json_search_found_categories
**Args:** $found_categories
**Tags:** #filter

### woocommerce_json_search_found_pages
**Args:** $pages_results
**Tags:** #filter

### woocommerce_json_search_limit
**Args:** 30
**Tags:** #filter

### woocommerce_kses_notice_allowed_tags
**Params:** array[]|string $allowed_tags
**Since:** 3.9.0 | **Tags:** #filter
Kses notice allowed tags.

### woocommerce_layered_nav_default_query_type
**Args:** 'and'
**Tags:** #filter

### woocommerce_leaderboards
**Args:** $leaderboards, $per_page, $after, $before, $persisted_query
**Tags:** #filter

### woocommerce_legacy_api_and_hpos_incompatibility_warning_text
**Params:** string $legacy_api_and_hpos_incompatibility_warning_text
**Since:** 8.9.0 | **Tags:** #filter
Filter to modify the warning text that appears in the HPOS section of the features settings page when the Legacy REST API plugin is active and the orders table is in use as the primary data store for orders.

### woocommerce_load_webhooks_limit
**Params:** int $limit
**Since:** 3.6.0 | **Tags:** #filter
Hook: woocommerce_load_webhooks_limit.

### woocommerce_local_pickup_methods
**Params:** string[] $local_pickup_methods
**Since:** 6.8.0 | **Tags:** #filter
Filters local pickup shipping methods.

### woocommerce_localisation_address_formats
**Args:** array(
					'default' => "{name}\n{company}\n{address_1}\n{address_2}\n{city}\n{state}\n{postcode}\n{country}",
					'AT'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'AU'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city} {state} {postcode}\n{country}",
					'BE'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'CA'      => "{company}\n{name}\n{address_1}\n{address_2}\n{city} {state_code} {postcode}\n{country}",
					'CH'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'CL'      => "{company}\n{name}\n{address_1}\n{address_2}\n{state}\n{postcode} {city}\n{country}",
					'CN'      => "{country} {postcode}\n{state}, {city}, {address_2}, {address_1}\n{company}\n{name}",
					'CZ'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'DE'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'DK'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'EE'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'ES'      => "{name}\n{company}\n{address_1}\n{address_2}\n{postcode} {city}\n{state}\n{country}",
					'FI'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'FR'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city_upper}\n{country}",
					'HK'      => "{company}\n{first_name} {last_name_upper}\n{address_1}\n{address_2}\n{city_upper}\n{state_upper}\n{country}",
					'HU'      => "{last_name} {first_name}\n{company}\n{city}\n{address_1}\n{address_2}\n{postcode}\n{country}",
					'IN'      => "{company}\n{name}\n{address_1}\n{address_2}\n{city} {postcode}\n{state}, {country}",
					'IS'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'IT'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode}\n{city}\n{state_upper}\n{country}",
					'JM'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city}\n{state}\n{postcode_upper}\n{country}",
					'JP'      => "{postcode}\n{state} {city} {address_1}\n{address_2}\n{company}\n{last_name} {first_name}\n{country}",
					'LI'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'NL'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'NO'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'NZ'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city} {postcode}\n{country}",
					'PL'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'PR'      => "{company}\n{name}\n{address_1} {address_2}\n{city} \n{country} {postcode}",
					'PT'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'RS'      => "{name}\n{company}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'SE'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'SI'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'SK'      => "{company}\n{name}\n{address_1}\n{address_2}\n{postcode} {city}\n{country}",
					'TR'      => "{name}\n{company}\n{address_1}\n{address_2}\n{postcode} {city} {state}\n{country}",
					'TW'      => "{company}\n{last_name} {first_name}\n{address_1}\n{address_2}\n{state}, {city} {postcode}\n{country}",
					'UG'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city}\n{state}, {country}",
					'US'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city}, {state_code} {postcode}\n{country}",
					'VN'      => "{name}\n{company}\n{address_1}\n{address_2}\n{city} {postcode}\n{country}",
				)
**Tags:** #filter

### woocommerce_log_directory
**Params:** string $dir
**Since:** 8.8.0 | **Tags:** #filter
Filter to change the directory for storing WooCommerce's log files.

### woocommerce_log_file_size_limit
**Params:** int $file_size_limit
**Since:** 3.4.0 | **Tags:** #filter
Filter the threshold size of a log file at which point it will get rotated.

### woocommerce_logger_add_message
**Params:** string $handle, string $message, string $level
**Tags:** #filter
Add a log entry. This is not the preferred method for adding log messages. Please use log() or any one of the level methods (debug(), info(), etc.). This method may be deprecated in the future.

### woocommerce_logger_days_to_retain_logs
**Params:** int $days
**Since:** 3.4.0 | **Tags:** #filter
Filter the retention period of log entries.

### woocommerce_logger_delete_expired_file
**Params:** bool $delete, File $file, int $timestamp
**Since:** 8.7.0 | **Tags:** #filter
Allows preventing an expired log file from being deleted.

### woocommerce_logger_handler_options
**Params:** array $handler_options
**Since:** 8.6.0 | **Tags:** #filter
Filter the list of logging handlers that can be set as the default handler.

### woocommerce_logger_log_message
**Params:** string $message, string $level, array $context, object $handler
**Since:** 3.1 | **Tags:** #filter
Filter the logging message. Returning null will prevent logging from occurring since 5.3.

### woocommerce_logging_class
**Args:** 'WC_Logger'
**Tags:** #filter

### woocommerce_marketing_channels
**Params:** MarketingChannelInterface[] $channels
**Tags:** #filter
Filter the list of registered marketing channels.

### woocommerce_marketing_menu_items
**Params:** array $items
**Since:** 4.1.0 | **Tags:** #filter
Filters marketing menu items.

### woocommerce_marketplace_menu_items
**Args:** $marketplace_pages
**Tags:** #filter

### woocommerce_marketplace_suppress_promotions
**Args:** false
**Tags:** #filter

### woocommerce_matched_rates
**Args:** $matched_tax_rates, $tax_class, $customer
**Tags:** #filter

### woocommerce_matched_tax_rates
**Args:** $matched_tax_rates, $country, $state, $postcode, $city, $tax_class
**Tags:** #filter

### woocommerce_maxmind_geolocation_database_path
**Params:** string $database_path
**Since:** 3.9.0 | **Tags:** #filter
Filter the geolocation database storage path.

### woocommerce_maxmind_geolocation_database_service
**Args:** null
**Tags:** #filter

### woocommerce_maxmind_geolocation_display_notices
**Params:** mixed $old_value, mixed $new_value
**Tags:** #filter
Remove the old missing license key notice when it no longer applies.

### woocommerce_maxmind_geolocation_update_database_periodically
**Params:** bool $bind_updater
**Since:** 3.9.0 | **Tags:** #filter
Allows for the automatic database update to be disabled. Note that MaxMind's TOS requires that the databases be updated or removed periodically.

### woocommerce_mcp_allow_insecure_transport
**Params:** bool $allowed, \WP_REST_Request $request
**Since:** 10.3.0 | **Tags:** #filter
Filter to allow insecure transport for MCP requests.

### woocommerce_mcp_include_ability
**Params:** bool $include, string $ability_id
**Since:** 10.3.0 | **Tags:** #filter
Filter to override MCP ability inclusion decision.

### woocommerce_migrator_platforms
**Params:** array $platforms
**Since:** 1.0.0 | **Tags:** #filter
Filters the list of registered migration platforms. External platform plugins should hook into this filter to register themselves. Each platform plugin is responsible for its own autoloading and initialization.

### woocommerce_min_password_strength
**Args:** 3
**Tags:** #filter

### woocommerce_navigation_connect_page_options
**Params:** array $options
**Tags:** #filter
Filter the options when connecting or registering a page. Use the `js_page` option to determine if registering.

### woocommerce_navigation_current_screen_id
**Params:** string|boolean $screen_id, WP_Screen $current_screen
**Since:** 3.9.0 | **Tags:** #filter
Filter the current screen ID for REST API requests.

### woocommerce_navigation_is_connected_page
**Params:** boolean $is_connected_page, array|boolean $current_page
**Tags:** #filter
Whether or not the current page is an existing page connected to this controller. Used to determine if the WooCommerce Admin header should be rendered.

### woocommerce_navigation_is_registered_page
**Params:** boolean $is_registered_page, array|boolean $current_page
**Tags:** #filter
Whether or not the current page was registered with this controller. Used to determine if this is a JS-powered WooCommerce Admin page.

### woocommerce_navigation_page_tab_sections
**Args:** array(
				'products'          => array( '', 'inventory', 'downloadable', 'download_urls', 'advanced' ),
				'shipping'          => array( '', 'options', 'classes', 'pickup_location' ),
				'checkout'          => array( WC_Gateway_BACS::ID, WC_Gateway_Cheque::ID, WC_Gateway_COD::ID, WC_Gateway_Paypal::ID ),
				'email'             => $wc_email_ids,
				'advanced'          => array(
					'',
					'keys',
					'webhooks',
					'woocommerce_com',
					'features',
					'blueprint',
				),
				'browse-extensions' => array( 'helper' ),
			)
**Tags:** #filter

### woocommerce_navigation_pages_with_tabs
**Args:** array(
				'wc-reports'  => 'orders',
				'wc-settings' => 'general',
				'wc-status'   => 'status',
				'wc-addons'   => 'browse-extensions',
			)
**Tags:** #filter

### woocommerce_note_statuses
**Args:** $allowed_statuses
**Tags:** #filter

### woocommerce_note_types
**Args:** $allowed_types
**Tags:** #filter

### woocommerce_note_where_clauses
**Params:** string $where_clauses, array $args, string $context
**Tags:** #filter
Filter the notes WHERE clause before retrieving the data. Allows modification of the notes select criterial.

### woocommerce_notice_types
**Args:** array( 'error', 'success', 'notice' )
**Tags:** #filter

### woocommerce_payment_gateway_add_payment_method_delay
**Args:** 20
**Tags:** #filter

### woocommerce_payment_gateway_get_new_payment_method_option_html
**Params:** string $html, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the saved payment method option.

### woocommerce_payment_gateway_get_new_payment_method_option_html_label
**Params:** string $label, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the saved payment method label.

### woocommerce_payment_gateway_get_saved_payment_method_option_html
**Params:** string $html, string $token, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the saved payment method HTML.

### woocommerce_payment_gateway_save_new_payment_method_option_html
**Params:** string $html, WC_Payment_Gateway $this
**Since:** 2.6.0 | **Tags:** #filter
Filter the saved payment method checkbox HTML

### woocommerce_payment_gateway_supports
**Params:** boolean $supports, string $feature, WC_Payment_Gateway $this
**Since:** 1.5.7 | **Tags:** #filter
Filter the gateway supported features.

### woocommerce_payment_gateways
**Args:** $load_gateways
**Tags:** #filter

### woocommerce_payment_successful_result
**Args:** $result, $order_id
**Tags:** #filter

### woocommerce_payment_token_class
**Params:** string $class, string $type
**Since:** 3.8.0 | **Tags:** #filter
Filter payment token class per type.

### woocommerce_paypal_args
**Args:** array_merge(
				$this->get_transaction_args( $order ),
				$this->get_line_item_args( $order, true )
			), $order
**Tags:** #filter

### woocommerce_paypal_capture_request
**Args:** $request, $order, $amount
**Tags:** #filter

### woocommerce_paypal_icon
**Params:** string $icon
**Since:** 10.6.0 | **Tags:** #filter
Filters the PayPal icon image.

### woocommerce_paypal_supported_currencies
**Params:** array $supported_currencies
**Since:** 2.0.0 | **Tags:** #filter
Filter the supported currencies for PayPal.

### woocommerce_permission_list
**Args:** $data_store->get_downloads_for_customer( $customer_id ), $customer_id
**Tags:** #filter

### woocommerce_placeholder_img
**Args:** $image_html, $size, $dimensions
**Tags:** #filter

### woocommerce_placeholder_img_src
**Args:** $src
**Tags:** #filter

### woocommerce_plugins_are_incompatible_with_feature_by_default
**Params:** bool $incompatible_by_default, string $feature_id
**Since:** 9.2.0 | **Tags:** #filter
Filter to determine if plugins that don't declare compatibility nor incompatibility with a given feature are to be considered incompatible with that feature.

### woocommerce_pre_delete_$THIS->OBJECT_TYPE
**Tags:** #filter

### woocommerce_prevent_automatic_wizard_redirect
**Args:** false
**Tags:** #filter

### woocommerce_print_r_alternatives
**Args:** $alternatives, $expression
**Tags:** #filter

### woocommerce_privacy_erase_download_personal_data
**Args:** $erasure_enabled, $email_address
**Tags:** #filter

### woocommerce_privacy_erase_personal_data_tokens
**Params:** array $response, array $tokens
**Since:** 3.4.0 | **Tags:** #filter
Allow extensions to remove data for tokens and adjust the response.

### woocommerce_privacy_export_download_personal_data
**Params:** array $personal_data, WC_Order $order
**Since:** 3.4.0 | **Tags:** #filter
Allow extensions to register their own personal data for this download for the export.

### woocommerce_process_login_errors
**Args:** $validation_error, $creds['user_login'], $creds['user_password']
**Tags:** #filter

### woocommerce_process_registration_errors
**Args:** $validation_error, $username, $password, $email
**Tags:** #filter

### woocommerce_queue_class
**Args:** self::$default_cass
**Tags:** #filter

### woocommerce_queued_js
**Params:** string $js
**Since:** 2.6.0 | **Tags:** #filter
Queued jsfilter.

### woocommerce_rate_code
**Args:** $code_string, $key
**Tags:** #filter

### woocommerce_rate_compound
**Args:** $compound, $key
**Tags:** #filter

### woocommerce_rate_label
**Args:** $rate_name, $key
**Tags:** #filter

### woocommerce_rate_percent
**Args:** $rate_percent_value . '%', $tax_rate_id
**Tags:** #filter

### woocommerce_redirect_only_method_is_secure
**Args:** false
**Tags:** #filter

### woocommerce_regenerate_images_intermediate_image_sizes
**Args:** $unfiltered_sizes
**Tags:** #filter

### woocommerce_registration_errors
**Params:** \WP_Error $errors, string $username, string $user_email
**Since:** 7.2.0 | **Tags:** #filter
Filters registration errors before a customer account is registered. This hook filters registration errors. This can be used to manipulate the array of errors before they are displayed.

### woocommerce_registration_redirect
**Args:** $redirect
**Tags:** #filter

### woocommerce_remote_logger_formatted_log_data
**Params:** array $log_data, string $level, string $message, array $context
**Since:** 9.2.0 | **Tags:** #filter
Filters the formatted log data before sending it to the remote logging service. Returning a non-array value will prevent the log from being sent.

### woocommerce_remote_logger_request_uri_whitelist
**Params:** string $default_whitelist
**Since:** 9.4.0 | **Tags:** #filter
Filter to allow other plugins to whitelist request_uri query parameter values for unmasked remote logging.

### woocommerce_remote_logger_sanitized_content
**Params:** string $sanitized, string $content
**Since:** 9.5.0 | **Tags:** #filter
Filter the sanitized log content before it's sent to the remote logging service.

### woocommerce_remote_logging_is_third_party_error
**Params:** bool $is_third_party_error, string $message, array $context
**Since:** 9.2.0 | **Tags:** #filter
Filter to allow other plugins to overwrite the result of the third-party error check for remote logging.

### woocommerce_report_categories_export_columns
**Args:** $export_columns
**Tags:** #filter

### woocommerce_report_categories_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_report_downloads_prepare_export_item
**Args:** $export_item, $item
**Tags:** #filter

### woocommerce_report_downloads_query_from
**Args:** $query_from
**Tags:** #filter

### woocommerce_report_recent_reviews_query_from
**Params:** string $clause
**Since:** 3.1.0 | **Tags:** #filter
Filters the from-clause used for fetching latest product reviews.

### woocommerce_report_revenue_stats_export_columns
**Params:** array $export_columns
**Since:** 10.7.0 | **Tags:** #filter
Filter to add or remove column names from the revenue stats report for export.

### woocommerce_report_revenue_stats_prepare_export_item
**Params:** array $export_item, array $item
**Since:** 10.7.0 | **Tags:** #filter
Filter to prepare extra columns in the export item for the revenue stats report.

### woocommerce_report_taxes_export_columns
**Params:** array $export_columns
**Since:** 10.7.0 | **Tags:** #filter
Filter to add or remove column names from the taxes report for export.

### woocommerce_report_taxes_prepare_export_item
**Params:** array $export_item, array $item
**Since:** 10.7.0 | **Tags:** #filter
Filter to prepare extra columns in the export item for the taxes report.

### woocommerce_reports_charts
**Args:** $reports
**Tags:** #filter

### woocommerce_reports_screen_ids
**Args:** array( $wc_screen_id . '_page_wc-reports', 'toplevel_page_wc-reports' )
**Tags:** #filter

### woocommerce_reports_taxes_rate
**Args:** $rate, $rate_id, $tax_row
**Tags:** #filter

### woocommerce_reports_taxes_tax_rate
**Args:** $tax_row->tax_rate, $rate_id, $tax_row
**Tags:** #filter

### woocommerce_resize_images
**Params:** array $image, int $attachment_id, string|array $size, bool $icon
**Tags:** #filter
Check if we should maybe generate a new image size if not already there.

### woocommerce_return_previous_exceptions
**Args:** Constants::is_true( 'WP_DEBUG' )
**Tags:** #filter

### woocommerce_sanitize_additional_field
**Params:** mixed $field_value, string $field_key
**Since:** 8.7.0 | **Tags:** #filter
Allow custom sanitization of an additional field.

### woocommerce_saved_payment_methods_list
**Params:** int $customer_id
**Since:** 2.6.0 | **Tags:** #filter
Get customer saved payment methods list.

### woocommerce_set_cookie_enabled
**Params:** bool $set_cookie_enabled, string $name, string $value, integer $expire, bool $secure
**Since:** 6.3.0 | **Tags:** #filter
Controls whether the cookie should be set via wc_setcookie().

### woocommerce_set_cookie_options
**Params:** array $cookie_options, string $name, string $value
**Since:** 6.7.0 | **Tags:** #filter
Controls the options to be specified when setting the cookie.

### woocommerce_setup_wizard_force_legacy
**Args:** false
**Tags:** #filter

### woocommerce_setup_wizard_steps
**Args:** $default_steps
**Tags:** #filter

### woocommerce_shop_manager_editable_roles
**Args:** array( 'customer' )
**Tags:** #filter

### woocommerce_should_load_brands_styles
**Params:** bool $should_load
**Since:** 10.4.0 | **Tags:** #filter
Filter whether brands styles should be loaded.

### woocommerce_show_addons_page
**Params:** bool $show_addons_page
**Since:** 8.2.1 | **Tags:** #filter
Controls whether we add a submenu item for the WooCommerce Addons page. Woo Express uses this filter.

### woocommerce_show_autoinstalled_plugin_notices
**Params:** bool $display_notice
**Since:** 8.8.0 | **Tags:** #filter
Filter to suppress the notice about autoinstalled plugins in the plugins list page.

### woocommerce_show_tax_configuration_notice
**Params:** bool $show_notice
**Since:** 10.5.0 | **Tags:** #filter
Filter whether to show the tax configuration incomplete notice.

### woocommerce_sort_countries
**Args:** true
**Tags:** #filter

### woocommerce_sortable_taxonomies
**Params:** array $sortable_taxonomies
**Since:** 1.0 | **Tags:** #filter
Filters the list of taxonomies that support custom ordering. Filter was introduced long ago is only documented in 10.6.0. First instance in plugins/woocommerce/includes/admin/class-wc-admin-assets.php.

### woocommerce_states
**Args:** $states
**Tags:** #filter

### woocommerce_store_api_disable_nonce_check
**Params:** boolean $disable_nonce_check
**Since:** 4.5.0 | **Tags:** #filter
Filters the Store API nonce check. This can be used to disable the nonce check when testing API endpoints via a REST API client.

### woocommerce_store_api_rate_limit_id
**Params:** string $id
**Since:** 9.8.0 | **Tags:** #filter
Filters the rate limiting identifier.

### woocommerce_store_api_rate_limit_options
**Params:** array $rate_limit_options
**Since:** 8.9.0 | **Tags:** #filter
Filters options for Rate Limits.

### woocommerce_store_pages
**Params:** array $store_pages
**Since:** 8.8.0 | **Tags:** #filter
Filter the store pages array to check if a URL is a store page.

### woocommerce_structured_data_context
**Args:** array( '@context' => 'https://schema.org/' ), $data, $type, $value
**Tags:** #filter

### woocommerce_structured_data_review
**Args:** $markup, $comment
**Tags:** #filter

### woocommerce_structured_data_type_for_page
**Args:** $types
**Tags:** #filter

### woocommerce_structured_data_website
**Args:** $markup
**Tags:** #filter

### woocommerce_style_smallscreen_breakpoint
**Args:** '768px'
**Tags:** #filter

### woocommerce_suggest_jetpack
**Args:** true
**Tags:** #filter

### woocommerce_support_url
**Args:** 'https://woocommerce.com/my-account/create-a-ticket/'
**Tags:** #filter

### woocommerce_system_status_environment_rows
**Args:** array()
**Tags:** #filter
Filters the environment rows to show in the WooCommerce status report.

### woocommerce_tax_round
**Params:** float|int $in
**Tags:** #filter
Round to precision. Filter example: to return rounding to .5 cents you'd use: function euro_5cent_rounding( $in ) { return round( $in / 5, 2 ) * 5; } add_filter( 'woocommerce_tax_round', 'euro_5cent_rounding' );

### woocommerce_thumbnail_size
**Params:** string $size
**Since:** 2.6.0 | **Tags:** #filter
Filters the thumbnail size.

### woocommerce_time_format
**Args:** $time_format
**Tags:** #filter

### woocommerce_tracker_data
**Args:** $data
**Tags:** #filter

### woocommerce_tracker_event_recurrence
**Params:** string $recurrence
**Since:** 2.3.0 | **Tags:** #filter
How frequent to schedule the tracker send event.

### woocommerce_tracker_last_send_interval
**Args:** strtotime( '-1 week' )
**Tags:** #filter

### woocommerce_tracker_last_send_time
**Args:** get_option( 'woocommerce_tracker_last_send', false )
**Tags:** #filter

### woocommerce_tracker_send_override
**Args:** $override
**Tags:** #filter

### woocommerce_tracks_event_properties
**Args:** $client_tracking_properties, false
**Tags:** #filter

### woocommerce_transient_files_directory
**Params:** string $transient_files_directory
**Since:** 8.5.0 | **Tags:** #filter
Filters the directory where transient files are stored. Note that this is used for both creating new files (with create_file_by_rendering_template) and retrieving existing files (with get_file_by_*).

### woocommerce_translations_updates_for_$PLUGINS[$PLUGIN][slug]
**Tags:** #filter

### woocommerce_twenty_nineteen_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_twenty_seventeen_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_twenty_twenty_one_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_twenty_twenty_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_twenty_twenty_three_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_twenty_twenty_two_styles
**Args:** $styles
**Tags:** #filter

### woocommerce_use_block_notices_in_classic_theme
**Params:** bool $use_block_notices_in_classic_theme
**Since:** 8.8.0 | **Tags:** #filter
Allow classic theme developers to opt-in to using block notices.

### woocommerce_use_xsendfile_for_remote
**Args:** false
**Tags:** #filter

### woocommerce_valid_location_types
**Params:** string $type
**Tags:** #filter
Is passed location type valid?

### woocommerce_valid_webhook_events
**Params:** array $valid_events
**Since:** 2.2.0 | **Tags:** #filter
Filters the list of valid webhook events.

### woocommerce_valid_webhook_resources
**Params:** array $valid_resources
**Since:** 2.2.0 | **Tags:** #filter
Filters the list of valid webhook resources.

### woocommerce_validate_postcode
**Args:** $valid, $postcode, $country
**Tags:** #filter

### woocommerce_vat_countries
**Args:** array_merge( $eu_countries, $vat_countries )
**Tags:** #filter

### woocommerce_version_string_generator_ttl
**Params:** int $ttl, string $id
**Since:** 10.4.0 | **Tags:** #filter
Filter the TTL for version string cache.

### woocommerce_version_string_invalidator_taxonomy_lookup_ttl
**Params:** int $ttl, string $entity_type
**Since:** 10.5.0 | **Tags:** #filter
Filters the cache TTL for queries that find entities associated with a term or taxonomy. These queries are used during cache invalidation to determine which entities (e.g., products, variations) need their cache cleared when a term or attribute changes.

### woocommerce_webhook_deliver_async
**Args:** true, $data['webhook'], $data['arg']
**Tags:** #filter

### woocommerce_webhook_event
**Args:** isset( $topic[1] ) ? $topic[1] : '', $this->get_id()
**Tags:** #filter

### woocommerce_webhook_hash_algorithm
**Params:** string $payload
**Since:** 2.2.0 | **Tags:** #filter
Generate a base64-encoded HMAC-SHA256 signature of the payload body so the recipient can verify the authenticity of the webhook. Note that the signature is calculated after the body has already been encoded (JSON by default).

### woocommerce_webhook_hooks
**Args:** $hooks, $this->get_id()
**Tags:** #filter

### woocommerce_webhook_http_args
**Params:** array $http_args, mixed $arg, int $webhook_id
**Since:** 3.3.0 | **Tags:** #filter
Filters the HTTP arguments for the webhook delivery.

### woocommerce_webhook_name
**Args:** $this->get_prop( 'name', $context ), $this->get_id()
**Tags:** #filter

### woocommerce_webhook_payload
**Params:** mixed $payload, string $resource, mixed $resource_id, int $webhook_id
**Since:** 2.2.0 | **Tags:** #filter
Filters the webhook payload before delivery.

### woocommerce_webhook_resource
**Args:** $topic[0], $this->get_id()
**Tags:** #filter

### woocommerce_webhook_secret
**Args:** $this->get_prop( 'secret', $context ), $this->get_id()
**Tags:** #filter

### woocommerce_webhook_should_deliver
**Params:** bool $should_deliver, WC_Webhook $this, mixed $arg
**Tags:** #filter
Let other plugins intercept deliver for some messages queue like rabbit/zeromq.

### woocommerce_webhook_status
**Args:** $this->get_prop( 'status', $context ), $this->get_id()
**Tags:** #filter

### woocommerce_webhook_statuses
**Args:** array(
			'active'   => __( 'Active', 'woocommerce' ),
			'paused'   => __( 'Paused', 'woocommerce' ),
			'disabled' => __( 'Disabled', 'woocommerce' ),
		)
**Tags:** #filter

### woocommerce_webhook_topic
**Args:** $this->get_prop( 'topic', $context ), $this->get_id()
**Tags:** #filter

### woocommerce_webhook_topic_hooks
**Params:** array $topic_hooks, WC_Webhook $webhook
**Since:** 2.2.0 | **Tags:** #filter
Filters the map of webhook topics to their registered hook names.

### woocommerce_webhook_topics
**Args:** array(
									''                  => __( 'Select an option&hellip;', 'woocommerce' ),
									'coupon.created'    => __( 'Coupon created', 'woocommerce' ),
									'coupon.updated'    => __( 'Coupon updated', 'woocommerce' ),
									'coupon.deleted'    => __( 'Coupon deleted', 'woocommerce' ),
									'coupon.restored'   => __( 'Coupon restored', 'woocommerce' ),
									'customer.created'  => __( 'Customer created', 'woocommerce' ),
									'customer.updated'  => __( 'Customer updated', 'woocommerce' ),
									'customer.deleted'  => __( 'Customer deleted', 'woocommerce' ),
									'order.created'     => __( 'Order created', 'woocommerce' ),
									'order.updated'     => __( 'Order updated', 'woocommerce' ),
									'order.deleted'     => __( 'Order deleted', 'woocommerce' ),
									'order.restored'    => __( 'Order restored', 'woocommerce' ),
									'product.created'   => __( 'Product created', 'woocommerce' ),
									'product.updated'   => __( 'Product updated', 'woocommerce' ),
									'product.deleted'   => __( 'Product deleted', 'woocommerce' ),
									'product.restored'  => __( 'Product restored', 'woocommerce' ),
									'product.published' => __( 'Product published', 'woocommerce' ),
									'action'            => __( 'Action', 'woocommerce' ),
								)
**Tags:** #filter

### wp_check_post_lock_window
**Args:** 150
**Tags:** #filter

### wp_plugin_dependencies_slug
**Params:** string $plugin_name
**Since:** 9.0.0 | **Tags:** #filter
Filters a plugin dependency’s slug before matching to the WordPress.org slug format.

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
