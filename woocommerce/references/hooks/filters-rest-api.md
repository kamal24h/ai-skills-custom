# WooCommerce Filters: REST API

> Core WooCommerce filter hooks, organized by domain. Sourced from the installed WooCommerce plugin's docblocks and call sites (v11.x).
> **Params:** typed parameters from docblocks · **Args:** raw arguments from the hook call site (no docblock available) · entries without either are name-only.

---

### rest_$THIS->GET_OBJECT_TYPE_additional_fields
**Tags:** #filter

### rest_$THIS->POST_TYPE_collection_params
**Tags:** #filter

### rest_additional_fields
**Params:** array $fields, string $object_type
**Since:** 10.2.0 | **Tags:** #filter
Filter additional fields for objects of this type.

### wc_rest_should_load_namespace
**Params:** bool $should_load, string $ns, string $rest_route, array $known_namespaces
**Since:** 9.4 | **Tags:** #filter
Filters whether a namespace should be loaded.

### woocommerce_admin_rest_controllers
**Params:** array $controllers
**Since:** 3.5.0 | **Tags:** #filter
Filter for the WooCommerce Admin REST controllers. Admin and Analytics controllers were originally loaded in one place.  However, with attempts to dynamically load namespaces based on context, these were split up.  However, to maintain backward compatibility, we must run this hook if either namespace is loaded because extensions could be targeting either namespace.

### woocommerce_api_key_last_access_datetime
**Args:** $date, $key['last_access']
**Tags:** #filter

### woocommerce_api_permissions_in_scope
**Args:** $permissions, $scope
**Tags:** #filter

### woocommerce_api_request_url
**Args:** $api_request_url, $request, $ssl
**Tags:** #filter

### woocommerce_apidocs_url
**Args:** 'https://woocommerce.com/wc-apidocs/'
**Tags:** #filter

### woocommerce_check_rest_ability_permissions_for_method
**Params:** bool $allowed, string $method, object $controller
**Since:** 10.3.0 | **Tags:** #filter
Filter to check REST ability permissions for HTTP method.

### woocommerce_disable_rest_api_access_log
**Params:** bool $result, int $key_id, int $user_id
**Since:** 7.7.0 | **Tags:** #filter
This filter enables the exclusion of the most recent access time from being logged for REST API calls.

### woocommerce_is_rest_api_request
**Args:** $is_rest_api_request
**Tags:** #filter

### woocommerce_rest_$OBJECT_TYPE_schema
**Tags:** #filter

### woocommerce_rest_$TAXONOMY_query
**Tags:** #filter

### woocommerce_rest_$THIS->POST_TYPE_object_query
**Tags:** #filter

### woocommerce_rest_$THIS->POST_TYPE_object_trashable
**Tags:** #filter

### woocommerce_rest_$THIS->POST_TYPE_query
**Tags:** #filter

### woocommerce_rest_$THIS->POST_TYPE_trashable
**Tags:** #filter

### woocommerce_rest_allowed_image_mime_types
**Args:** array(
			'jpg|jpeg|jpe' => 'image/jpeg',
			'gif'          => 'image/gif',
			'png'          => 'image/png',
			'bmp'          => 'image/bmp',
			'tiff|tif'     => 'image/tiff',
			'ico'          => 'image/x-icon',
			'webp'         => 'image/webp',
		)
**Tags:** #filter

### woocommerce_rest_api_cache_allowed_file_directories
**Params:** array $allowed_directories, object $controller
**Since:** 10.6.0 | **Tags:** #filter
Filter the directories allowed for file-based REST API response caching. This filter allows extensions to add additional directories that can contain files tracked for cache invalidation. The first directory in the array is used as the base path for resolving relative file paths.

### woocommerce_rest_api_cache_file_warning_suppression_ttl
**Params:** int $ttl, string $file_path, string $reason
**Since:** 10.6.0 | **Tags:** #filter
Filter the TTL for suppressing duplicate file tracking warnings. By default, each unique warning (file path + reason) is logged only once per hour to avoid flooding the log. Use this filter to customize the suppression period. Return 0 to disable suppression and log all warnings.

### woocommerce_rest_api_cache_files_hash_data
**Params:** array $files_data, array $file_paths, object $controller
**Since:** 10.6.0 | **Tags:** #filter
Filter the file data used for REST API response cache invalidation. This filter allows modification of the file tracking data before it is stored in the cache and used for invalidation checks.

### woocommerce_rest_api_cache_hooks_hash_data
**Params:** array $cache_hash_data, array $hook_names, object $controller
**Since:** 10.5.0 | **Tags:** #filter
Filter the data used to generate the hooks hash for REST API response caching.

### woocommerce_rest_api_cache_key_info
**Params:** array $cache_key_parts, bool $vary_by_user, string|null $endpoint_id, object $controller
**Since:** 10.5.0 | **Tags:** #filter
Filter the information used to generate the cache key for a REST API request. Allows customization of what uniquely identifies a request for caching purposes.

### woocommerce_rest_api_cache_settings
**Params:** array $settings
**Since:** 10.5.0 | **Tags:** #filter
Filter REST API cache settings.

### woocommerce_rest_api_cache_version_strings_hash_data
**Params:** array $version_data, array $version_string_ids, object $controller
**Since:** 10.6.0 | **Tags:** #filter
Filter the version strings data used for REST API response cache invalidation.

### woocommerce_rest_api_cached_headers
**Params:** array $cached_header_names, array $all_header_names, WP_REST_Request $request, WP_REST_Response $response, string|null $endpoint_id, object $controller
**Since:** 10.5.0 | **Tags:** #filter
Filter the list of response header names to cache.

### woocommerce_rest_api_enable_response_caching
**Params:** bool $enable_caching, object $controller
**Since:** 10.5.0 | **Tags:** #filter
Filter whether to enable response caching for a given REST API controller.

### woocommerce_rest_api_get_rest_namespaces
**Params:** array $controllers
**Since:** 4.5.0 | **Tags:** #filter
Filter the list of REST API controllers to load.

### woocommerce_rest_api_not_modified_response
**Params:** WP_REST_Response|false $response, WP_REST_Request $request, string|null $endpoint_id
**Since:** 10.5.0 | **Tags:** #filter
Filter the 304 Not Modified response before sending.

### woocommerce_rest_api_valid_to_save
**Args:** ! in_array( $current_section, array( 'keys', 'webhooks' ), true )
**Tags:** #filter

### woocommerce_rest_batch_items_limit
**Params:** array $items
**Tags:** #filter
Check batch limit.

### woocommerce_rest_check_permissions
**Params:** bool $permission, string $context, int $object_id, string $object_type
**Since:** 2.6.0 | **Tags:** #filter
Provides an opportunity to override the permission check made before acting on an object in relation to REST API requests.

### woocommerce_rest_customer_allowed_roles
**Params:** array $roles
**Since:** 9.5.2 | **Tags:** #filter
Filter the allowed roles for the REST API. Danger: Make sure that the roles listed here cannot manage the shop.

### woocommerce_rest_customer_query
**Params:** array $prepared_args, WP_REST_Request $request
**Tags:** #filter
Filter arguments, before passing to WP_User_Query, when querying users via the REST API.

### woocommerce_rest_is_request_to_rest_api
**Args:** $woocommerce || $third_party
**Tags:** #filter

### woocommerce_rest_notes_object_query
**Params:** array $args, WP_REST_Request $request
**Since:** 3.9.0 | **Tags:** #filter
Filter the query arguments for a request. Enables adding extra arguments or setting defaults for a post collection request.

### woocommerce_rest_onboarding_prepare_profile
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Since:** 6.5.0 | **Tags:** #filter
Filter the list returned from the API.

### woocommerce_rest_onboarding_profile_collection_params
**Params:** array $params
**Since:** 6.5.0 | **Tags:** #filter
Filters the Onboarding Profile REST API collection parameters.

### woocommerce_rest_onboarding_profile_object_query
**Params:** array $args, array $params
**Since:** 6.5.0 | **Tags:** #filter
Filter the query arguments for a request. Enables adding extra arguments or setting defaults for a post collection request.

### woocommerce_rest_onboarding_profile_properties
**Params:** array $properties
**Since:** 6.5.0 | **Tags:** #filter
Filters the Onboarding Profile REST API JSON Schema.

### woocommerce_rest_order_actions_email_preferred_template_ids
**Params:** string[] $preferred_template_ids, WC_Order $order, string[] $available
**Since:** 10.7.0 | **Tags:** #filter
Filter the preferred template IDs for auto-selecting an email template. Template IDs earlier in the array are preferred. Only templates that are also in the available templates list will be considered.

### woocommerce_rest_order_actions_email_valid_template_classes
**Params:** string[] $valid_template_classes, WC_Order $order
**Since:** 9.8.0 | **Tags:** #filter
Filter the list of valid email templates for a given order. Note that the email class must also exist in WC_Emails::$emails. When adding a custom email template to this list, a callback must also be added to trigger the sending of the email. See the `woocommerce_rest_order_actions_email_send` action hook.

### woocommerce_rest_orders_prepare_object_query
**Params:** array $args, WP_REST_Request $request
**Since:** 4.5.0. | **Tags:** #filter
Filter the query arguments for a request. Enables adding extra arguments or setting defaults for an order collection request.

### woocommerce_rest_performance_indicators_data_value
**Args:** $data, $stat, $report, $chart, $query_args
**Tags:** #filter

### woocommerce_rest_performance_indicators_jetpack_items
**Args:** array(
				'stats/visitors' => array(
					'label'      => __( 'Visitors', 'woocommerce' ),
					'permission' => 'view_stats',
					'format'     => 'number',
					'module'     => 'stats',
				),
				'stats/views'    => array(
					'label'      => __( 'Views', 'woocommerce' ),
					'permission' => 'view_stats',
					'format'     => 'number',
					'module'     => 'stats',
				),
			)
**Tags:** #filter

### woocommerce_rest_pre_insert_$THIS->POST_TYPE
**Tags:** #filter

### woocommerce_rest_pre_insert_$THIS->POST_TYPE_object
**Tags:** #filter

### woocommerce_rest_pre_insert_product_review
**Params:** array|WP_Error $prepared_review, WP_REST_Request $request
**Since:** 3.5.0 | **Tags:** #filter
Filters a review before it is inserted via the REST API. Allows modification of the review right before it is inserted via wp_insert_comment(). Returning a WP_Error value from the filter will shortcircuit insertion and allow skipping further processing.

### woocommerce_rest_prepare_$THIS->POST_TYPE
**Tags:** #filter

### woocommerce_rest_prepare_$THIS->POST_TYPE_object
**Tags:** #filter

### woocommerce_rest_prepare_$THIS->TAXONOMY
**Tags:** #filter

### woocommerce_rest_prepare_customer
**Params:** WP_REST_Response $response, WP_User $user_data, WP_REST_Request $request
**Tags:** #filter
Filter customer data returned from the REST API.

### woocommerce_rest_prepare_customer_download
**Params:** WP_REST_Response $response, stdObject $download, WP_REST_Request $request
**Tags:** #filter
Filter customer download data returned from the REST API.

### woocommerce_rest_prepare_data_continent
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter the location list returned from the API. Allows modification of the location data right before it is returned.

### woocommerce_rest_prepare_data_country
**Params:** WP_REST_Response $response, array $data, WP_REST_Request $request
**Since:** 3.5.0 | **Tags:** #filter
Filter the states list for a country returned from the API. Allows modification of the location data right before it is returned.

### woocommerce_rest_prepare_data_currency
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter currency returned from the API.

### woocommerce_rest_prepare_data_download_ip
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter the list returned from the API.

### woocommerce_rest_prepare_fulfillments_providers
**Params:** array $providers, WP_REST_Request $request
**Since:** 10.5.0 | **Tags:** #filter
Filters the shipping providers response before it is returned. Each provider in the array must have the following structure: - 'label' (string): The display name of the provider. - 'icon' (string): URL to the provider's icon. - 'value' (string): The provider's unique identifier. - 'url' (string): The tracking URL template.

### woocommerce_rest_prepare_leaderboard
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter the list returned from the API.

### woocommerce_rest_prepare_note
**Params:** WP_REST_Response $response, array $data, WP_REST_Request $request
**Since:** 3.9.0 | **Tags:** #filter
Filter a note returned from the API. Allows modification of the note data right before it is returned.

### woocommerce_rest_prepare_order_note
**Params:** WP_REST_Response $response, WP_Comment $note, WP_REST_Request $request
**Tags:** #filter
Filter order note object returned from the REST API.

### woocommerce_rest_prepare_payment_gateway
**Params:** WP_REST_Response $response, WC_Payment_Gateway $gateway, WP_REST_Request $request
**Tags:** #filter
Filter payment gateway objects returned from the REST API.

### woocommerce_rest_prepare_product_attribute
**Params:** WP_REST_Response $response, object $item, WP_REST_Request $request
**Tags:** #filter
Filter a attribute item returned from the API. Allows modification of the product attribute data right before it is returned.

### woocommerce_rest_prepare_product_review
**Params:** WP_REST_Response $response, WP_Comment $review, WP_REST_Request $request
**Tags:** #filter
Filter product reviews object returned from the REST API.

### woocommerce_rest_prepare_report
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_categories
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_coupons
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_coupons_count
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_coupons_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_customers
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Since:** 4.0.0 | **Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_customers_count
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_customers_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_downloads
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_downloads_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_orders
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_orders_count
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_orders_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_performance_indicators
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_products
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Since:** 6.5.0 | **Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_products_count
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_products_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_revenue_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_reviews_count
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_sales
**Params:** WP_REST_Response $response, stdClass $data, WP_REST_Request $request
**Tags:** #filter
Filter a report sales returned from the API. Allows modification of the report sales data right before it is returned.

### woocommerce_rest_prepare_report_stock
**Params:** WP_REST_Response $response, WC_Product $product, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_stock_stats
**Params:** WP_REST_Response $response, WC_Product $report, WP_REST_Request $request
**Since:** 6.5.0 | **Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_taxes
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_taxes_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_top_sellers
**Params:** WP_REST_Response $response, stdClass $top_seller, WP_REST_Request $request
**Tags:** #filter
Filter a report top sellers returned from the API. Allows modification of the report top sellers data right before it is returned.

### woocommerce_rest_prepare_report_variations
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Since:** 6.5.0 | **Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_report_variations_stats
**Params:** WP_REST_Response $response, object $report, WP_REST_Request $request
**Tags:** #filter
Filter a report returned from the API. Allows modification of the report data right before it is returned.

### woocommerce_rest_prepare_reports_import
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter the list returned from the API.

### woocommerce_rest_prepare_shipping_method
**Params:** WP_REST_Response $response, WC_Shipping_Method $method, WP_REST_Request $request
**Tags:** #filter
Filter shipping methods object returned from the REST API.

### woocommerce_rest_prepare_system_status
**Params:** WP_REST_Response $response, mixed $system_status, WP_REST_Request $request
**Tags:** #filter
Filter the system status returned from the REST API.

### woocommerce_rest_prepare_tax
**Params:** WP_REST_Response $response, stdClass $tax_class, WP_REST_Request $request
**Tags:** #filter
Filter tax object returned from the REST API.

### woocommerce_rest_prepare_themes
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Tags:** #filter
Filter the list returned from the API.

### woocommerce_rest_prepare_webhook_delivery
**Params:** WP_REST_Response $response, stdClass $log, WP_REST_Request $request
**Tags:** #filter
Filter webhook delivery object returned from the REST API.

### woocommerce_rest_private_query_vars
**Params:** array $private_query_vars
**Tags:** #filter
Filter the allowed 'private' query vars for authorized users. If the user has the `edit_posts` capability, we also allow use of private query parameters, which are only undesirable on the frontend, but are safe for use in query strings. To disable anyway, use `add_filter( 'woocommerce_rest_private_query_vars', '__return_empty_array' );`

### woocommerce_rest_product_review_collection_params
**Params:** array $params
**Since:** 3.5.0 | **Tags:** #filter
Filter collection parameters for the reviews controller. This filter registers the collection parameter, but does not map the collection parameter to an internal WP_Comment_Query parameter. Use the `wc_rest_review_query` filter to set WP_Comment_Query parameters.

### woocommerce_rest_product_review_query
**Params:** array $prepared_args, WP_REST_Request $request
**Since:** 3.5.0 | **Tags:** #filter
Filters arguments, before passing to WP_Comment_Query, when querying reviews via the REST API.

### woocommerce_rest_product_review_trashable
**Params:** bool $supports_trash, WP_Comment $review
**Since:** 3.5.0 | **Tags:** #filter
Filters whether a review can be trashed. Return false to disable trash support for the post.

### woocommerce_rest_query_var-$VAR
**Tags:** #filter

### woocommerce_rest_query_vars
**Args:** $valid_vars
**Tags:** #filter

### woocommerce_rest_refunds_prepare_object_query
**Params:** array $args, WP_REST_Request $request
**Since:** 9.0.0. | **Tags:** #filter
Filter the query arguments for a request. Enables adding extra arguments or setting defaults for an order collection request.

### woocommerce_rest_report_sort_performance_indicators
**Params:** array $indicators
**Tags:** #filter
Custom ordering for store performance indicators.

### woocommerce_rest_reports_column_types
**Args:** $this->column_types, $array
**Tags:** #filter

### woocommerce_rest_reports_products_extended_attributes
**Args:** $this->extended_attributes, $product_data
**Tags:** #filter

### woocommerce_rest_reports_variations_extended_attributes
**Args:** $this->extended_attributes, $product_data
**Tags:** #filter

### woocommerce_rest_should_lazy_load_namespace
**Params:** bool $should_lazy_load_namespace, string $route_namespace
**Since:** 10.3.0 | **Tags:** #filter
Filter whether to lazy load the namespace.  When set to false, the namespace will be loaded immediately during initialization.

### woocommerce_rest_suppress_image_upload_error
**Params:** array $upload
**Since:** 4.5.0 | **Tags:** #filter
Filter to check if it should suppress the image upload error, false by default.

### woocommerce_rest_tax_query
**Params:** array $prepared_args, WP_REST_Request $request
**Tags:** #filter
Filter arguments, before passing to $wpdb->get_results(), when querying taxes via the REST API.

### woocommerce_rest_themes_collection_params
**Args:** $params
**Tags:** #filter

### woocommerce_rest_webhook_query
**Params:** array $args, WP_REST_Request $request
**Tags:** #filter
Filter arguments, before passing to WC_Webhook_Data_Store->search_webhooks, when querying webhooks via the REST API.

### woocommerce_restock_refunded_items
**Args:** true
**Tags:** #filter

### woocommerce_restored_session_data
**Params:** array $session_data
**Since:** 9.9.0 | **Tags:** #filter
Filters the session data when restoring from storage during initialization. This filter allows you to: 1. Modify the session data before it's loaded, including adding or removing specific session data entries 2. Clear the entire session by returning an empty array Note: If the filtered data is empty, the session will be destroyed and the guest's session cookie will be removed. This can be useful for high-traffic sites that prioritize page caching over maintaining all session data.

### woocommerce_skip_legacy_rest_api_plugin_auto_install
**Tags:** #filter

## Sources

- [WooCommerce Code Reference — Hooks](https://woocommerce.github.io/code-reference/hooks/hooks.html)
- [WooCommerce Action & Filter Hook Reference](https://woocommerce.com/document/wc_api-the-woocommerce-api-callbacks/)
- Extracted from local WooCommerce plugin source (`do_action` / `apply_filters` calls)
