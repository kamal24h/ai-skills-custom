# WordPress Filters: REST API / oEmbed

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### embed_cache_oembed_types
**Params:** string[] $post_types
**Since:** 2.9 | **Tags:** #Legacy
Filters the array of post types to cache oEmbed results for.

### embed_defaults
**Params:** int[] $size, string $url
**Since:** 2.9 | **Tags:** #Legacy
Filters the default array of embed dimensions.

### embed_handler_html
**Params:** string $return, string $url, array $attr
**Since:** 2.9 | **Tags:** #Legacy
Filters the returned embed HTML.

### embed_maybe_make_link
**Params:** string $output, string $url
**Since:** 2.9 | **Tags:** #Legacy
Filters the returned, maybe-linked embed URL.

### embed_oembed_discover
**Since:** 2.9 | **Tags:** #Legacy

### embed_oembed_html
**Params:** string $cache, string $url, array $attr, int $post_id
**Since:** 2.9 | **Tags:** #Legacy
Filters the cached oEmbed HTML.

### oembed_dataparse
**Params:** string|false $return, object $data, string $url
**Since:** 2.9 | **Tags:** #Legacy
Filters the returned oEmbed HTML. Use this filter to add support for custom data types, or to filter the result.

### oembed_linktypes
**Params:** string[] $format
**Since:** 2.9 | **Tags:** #Legacy
Filters the link types that contain oEmbed provider URLs.

### oembed_providers
**Since:** 2.9 | **Tags:** #Legacy

### oembed_result
**Params:** string|false $data, string $url, string|array $args
**Since:** 2.9 | **Tags:** #Legacy
Filters the HTML returned by the oEmbed provider.

### oembed_fetch_url
**Params:** string $provider, string $url, array $args
**Since:** 3.5 | **Tags:** #Modern
Filters the oEmbed URL to be fetched.

### oembed_remote_get_args
**Params:** array $args, string $url
**Since:** 4.0 | **Tags:** #Modern
Filters oEmbed remote get arguments.

### oembed_ttl
**Params:** int $time, string $url, array $attr, int $post_id
**Since:** 4.0 | **Tags:** #Modern
Filters the oEmbed TTL value (time to live).

### embed_html
**Params:** string $output, WP_Post $post, int $width, int $height
**Since:** 4.4 | **Tags:** #Modern
Filters the embed HTML output for a given post.

### embed_site_title_html
**Params:** string $site_title
**Since:** 4.4 | **Tags:** #Modern
Filters the site title HTML in the embed footer.

### embed_thumbnail_image_shape
**Params:** string $shape, int $thumbnail_id
**Since:** 4.4 | **Tags:** #Modern
Filters the thumbnail shape for use in the embed template. Rectangular images are shown above the title while square images are shown next to the content.

### embed_thumbnail_image_size
**Params:** string $image_size, int $thumbnail_id
**Since:** 4.4 | **Tags:** #Modern
Filters the thumbnail image size for use in the embed template.

### oembed_default_width
**Params:** int $maxwidth
**Since:** 4.4 | **Tags:** #Modern
Filters the maxwidth oEmbed parameter.

### oembed_discovery_links
**Params:** string $output
**Since:** 4.4 | **Tags:** #Modern
Filters the oEmbed discovery links HTML.

### oembed_endpoint_url
**Params:** string $url, string $permalink, string $format
**Since:** 4.4 | **Tags:** #Modern
Filters the oEmbed endpoint URL.

### oembed_min_max_width
**Params:** array $min_max_width
**Since:** 4.4 | **Tags:** #Modern
Filters the allowed minimum and maximum widths for the oEmbed response.

### oembed_request_post_id
**Params:** int $post_id, string $url
**Since:** 4.4 | **Tags:** #Modern
Filters the determined post ID.

### oembed_response_data
**Params:** array $data, WP_Post $post, int $width, int $height
**Since:** 4.4 | **Tags:** #Modern
Filters the oEmbed response data.

### rest_authentication_errors
**Params:** WP_Error|null|true $errors
**Since:** 4.4 | **Tags:** #Modern
Filters REST API authentication errors. This is used to pass a WP_Error from an authentication method back to the API. Authentication methods should check first if they're being used, as multiple authentication methods can be enabled on a site (cookies, HTTP basic auth, OAuth). If the authentication method hooked in is not actually being attempted, null should be returned to indicate another authentication method should check instead. Similarly, callbacks should ensure the value is `null` before checking for errors. A WP_Error instance can be returned if an error occurs, and this should match the format used by API methods internally (that is, the `status` data should be used). A callback can return `true` to indicate that the authentication method was used, and it succeeded.

### rest_dispatch_request
**Params:** mixed $dispatch_result, WP_REST_Request $request, string $route, array $handler
**Since:** 4.4 | **Tags:** #Modern
Filters the REST API dispatch request result. Allow plugins to override dispatching the request.

### rest_endpoints
**Params:** array $endpoints
**Since:** 4.4 | **Tags:** #Modern
Filters the array of available REST API endpoints.

### rest_endpoints_description
**Params:** array $data
**Since:** 4.4 | **Tags:** #Modern
Filters the publicly-visible data for a single REST API route.

### rest_envelope_response
**Params:** array $envelope, WP_REST_Response $response
**Since:** 4.4 | **Tags:** #Modern
Filters the enveloped form of a REST API response.

### rest_index
**Params:** WP_REST_Response $response, WP_REST_Request $request
**Since:** 4.4 | **Tags:** #Modern
Filters the REST API root index data. This contains the data describing the API. This includes information about supported authentication schemes, supported namespaces, routes available on the API, and a small amount of data about the site.

### rest_jsonp_enabled
**Params:** bool $jsonp_enabled
**Since:** 4.4 | **Tags:** #Modern
Filters whether JSONP is enabled for the REST API.

### rest_namespace_index
**Params:** WP_REST_Response $response, WP_REST_Request $request
**Since:** 4.4 | **Tags:** #Modern
Filters the REST API namespace index data. This typically is just the route data for the namespace, but you can add any data you'd like here.

### rest_post_dispatch
**Params:** WP_HTTP_Response $result, WP_REST_Server $server, WP_REST_Request $request
**Since:** 4.4 | **Tags:** #Modern
Filters the REST API response. Allows modification of the response before returning.

### rest_pre_dispatch
**Params:** mixed $result, WP_REST_Server $server, WP_REST_Request $request
**Since:** 4.4 | **Tags:** #Modern
Filters the pre-calculated result of a REST API dispatch request. Allow hijacking the request before dispatching by returning a non-empty. The returned value will be used to serve the request instead.

### rest_pre_serve_request
**Params:** bool $served, WP_HTTP_Response $result, WP_REST_Request $request, WP_REST_Server $server
**Since:** 4.4 | **Tags:** #Modern
Filters whether the REST API request has already been served. Allow sending the request manually - by returning true, the API result will not be sent to the client.

### rest_request_parameter_order
**Params:** string[] $order, WP_REST_Request $request
**Since:** 4.4 | **Tags:** #Modern
Filters the parameter priority order for a REST API request. The order affects which parameters are checked when using WP_REST_Request::get_param() and family. This acts similarly to PHP's `request_order` setting.

### rest_route_data
**Params:** array[] $available, array $routes
**Since:** 4.4 | **Tags:** #Modern
Filters the publicly-visible data for REST API routes. This data is exposed on indexes and can be used by clients or developers to investigate the site and find out how to use it. It acts as a form of self-documentation.

### rest_send_nocache_headers
**Params:** bool $rest_send_nocache_headers
**Since:** 4.4 | **Tags:** #Modern
Filters whether to send no-cache headers on a REST API request.

### rest_url
**Params:** string $url, string $path, int|null $blog_id, string $scheme
**Since:** 4.4 | **Tags:** #Modern
Filters the REST URL. Use this filter to adjust the url returned by the get_rest_url() function.

### rest_url_prefix
**Params:** string $prefix
**Since:** 4.4 | **Tags:** #Modern
Filters the REST URL prefix.

### wp_rest_server_class
**Params:** string $class_name
**Since:** 4.4 | **Tags:** #Modern
Filters the REST Server Class. This filter allows you to adjust the server class used by the REST API, using a different class to handle requests.

### rest_request_from_url
**Params:** WP_REST_Request|false $request, string $url
**Since:** 4.5 | **Tags:** #Modern
Filters the REST API request generated from a URL.

### rest_response_link_curies
**Params:** array $additional
**Since:** 4.5 | **Tags:** #Modern
Filters extra CURIEs available on REST API responses. CURIEs allow a shortened version of URI relations. This allows a more usable form for custom relations than using the full URI. These work similarly to how XML namespaces work. Registered CURIES need to specify a name and URI template. This will automatically transform URI relations into their shortened version. The shortened relation follows the format `{name}:{rel}`. `{rel}` in the URI template will be replaced with the `{rel}` part of the shortened relation. For example, a CURIE with name `example` and URI template `http://w.org/{rel}` would transform a `http://w.org/term` relation into `example:term`. Well-behaved clients should expand and normalize these back to their full URI relation, however some naive clients may not resolve these correctly, so adding new CURIEs may break backward compatibility.

### pre_oembed_result
**Params:** null|string $result, string $url, string|array $args
**Since:** 4.6 | **Tags:** #Modern
Filters the oEmbed result before any HTTP requests are made. This allows one to short-circuit the default logic, perhaps by replacing it with a routine that is more optimal for your setup. Returning a non-null value from the filter will effectively short-circuit retrieval and return the passed value instead.

### rest_allow_anonymous_comments
**Params:** bool $allow_anonymous, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters whether comments can be created via the REST API without authentication. Enables creating comments for anonymous users.

### rest_avatar_sizes
**Params:** int[] $sizes
**Since:** 4.7 | **Tags:** #Modern
Filters the REST avatar sizes. Use this filter to adjust the array of sizes returned by the `rest_get_avatar_sizes` function.

### rest_comment_collection_params
**Params:** array $query_params
**Since:** 4.7 | **Tags:** #Modern
Filters REST API collection parameters for the comments controller. This filter registers the collection parameter, but does not map the collection parameter to an internal WP_Comment_Query parameter. Use the `rest_comment_query` filter to set WP_Comment_Query parameters.

### rest_comment_query
**Params:** array $prepared_args, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters WP_Comment_Query arguments when querying comments via the REST API.

### rest_comment_trashable
**Params:** bool $supports_trash, WP_Comment $comment
**Since:** 4.7 | **Tags:** #Modern
Filters whether a comment can be trashed via the REST API. Return false to disable trash support for the comment.

### rest_prepare_attachment
**Params:** WP_REST_Response $response, WP_Post $post, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters an attachment returned from the REST API. Allows modification of the attachment right before it is returned.

### rest_prepare_comment
**Params:** WP_REST_Response $response, WP_Comment $comment, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a comment returned from the REST API. Allows modification of the comment right before it is returned.

### rest_prepare_post_type
**Params:** WP_REST_Response $response, WP_Post_Type $post_type, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a post type returned from the REST API. Allows modification of the post type data right before it is returned.

### rest_prepare_revision
**Params:** WP_REST_Response $response, WP_Post $post, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a revision returned from the REST API. Allows modification of the revision right before it is returned.

### rest_prepare_status
**Params:** WP_REST_Response $response, object $status, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a post status returned from the REST API. Allows modification of the status data right before it is returned.

### rest_prepare_taxonomy
**Params:** WP_REST_Response $response, WP_Taxonomy $item, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a taxonomy returned from the REST API. Allows modification of the taxonomy data right before it is returned.

### rest_prepare_user
**Params:** WP_REST_Response $response, WP_User $user, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters user data returned from the REST API.

### rest_prepare_{$this->post_type}
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_prepare_{$this->taxonomy}
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_preprocess_comment
**Params:** array $prepared_comment, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a comment added via the REST API after it is prepared for insertion into the database. Allows modification of the comment right after it is prepared for the database.

### rest_pre_get_setting
**Params:** mixed $result, string $name, array $args
**Since:** 4.7 | **Tags:** #Modern
Filters the value of a setting recognized by the REST API. Allow hijacking the setting value and overriding the built-in behavior by returning a non-null value.  The returned value will be presented as the setting value instead.

### rest_pre_insert_comment
**Params:** array|WP_Error $prepared_comment, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters a comment before it is inserted via the REST API. Allows modification of the comment right before it is inserted via wp_insert_comment(). Returning a WP_Error value from the filter will short-circuit insertion and allow skipping further processing.

### rest_pre_insert_user
**Params:** object $prepared_user, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters user data before insertion via the REST API.

### rest_pre_insert_{$this->post_type}
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_pre_insert_{$this->taxonomy}
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_pre_update_setting
**Params:** bool $result, string $name, mixed $value, array $args
**Since:** 4.7 | **Tags:** #Modern
Filters whether to preempt a setting value update via the REST API. Allows hijacking the setting update logic and overriding the built-in behavior by returning true.

### rest_query_var-{$key}
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_request_after_callbacks
**Params:** WP_REST_Response|WP_HTTP_Response|WP_Error|mixed $response, array $handler, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters the response immediately after executing any REST API callbacks. Allows plugins to perform any needed cleanup, for example, to undo changes made during the {@see 'rest_request_before_callbacks'} filter. Note that this filter will not be called for requests that fail to authenticate or match to a registered route. Note that an endpoint's `permission_callback` can still be called after this filter - see `rest_send_allow_header()`.

### rest_request_before_callbacks
**Params:** WP_REST_Response|WP_HTTP_Response|WP_Error|mixed $response, array $handler, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters the response before executing any REST API callbacks. Allows plugins to perform additional validation after a request is initialized and matched to a registered route, but before it is executed. Note that this filter will not be called for requests that fail to authenticate or match to a registered route.

### rest_user_collection_params
**Params:** array $query_params
**Since:** 4.7 | **Tags:** #Modern
Filters REST API collection parameters for the users controller. This filter registers the collection parameter, but does not map the collection parameter to an internal WP_User_Query parameter.  Use the `rest_user_query` filter to set WP_User_Query arguments.

### rest_user_query
**Params:** array $prepared_args, WP_REST_Request $request
**Since:** 4.7 | **Tags:** #Modern
Filters WP_User_Query arguments when querying users via the REST API.

### rest_{$this->post_type}_collection_params
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_{$this->post_type}_query
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_{$this->post_type}_trashable
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_{$this->taxonomy}_collection_params
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_{$this->taxonomy}_query
**Since:** 4.7 | **Tags:** #Variable #Modern

### rest_oembed_ttl
**Params:** int $time, string $url, array $args
**Since:** 4.8 | **Tags:** #Modern
Filters the oEmbed TTL value (time to live). Similar to the {@see 'oembed_ttl'} filter, but for the REST API oEmbed proxy endpoint.

### embed_thumbnail_id
**Params:** int|false $thumbnail_id
**Since:** 4.9 | **Tags:** #Modern
Filters the thumbnail image ID for use in the embed template.

### rest_pre_echo_response
**Params:** array $result, WP_REST_Server $server, WP_REST_Request $request
**Since:** 4.9 | **Tags:** #Modern
Filters the REST API response. Allows modification of the response data after inserting embedded data (if any) and before echoing the response data.

### rest_prepare_autosave
**Params:** WP_REST_Response $response, WP_Post $post, WP_REST_Request $request
**Since:** 5.0 | **Tags:** #Recent
Filters a revision returned from the REST API. Allows modification of the revision right before it is returned.

### rest_prepare_theme
**Params:** WP_REST_Response $response, WP_Theme $theme, WP_REST_Request $request
**Since:** 5.0 | **Tags:** #Recent
Filters theme data returned from the REST API.

### rest_revision_query
**Params:** array $args, WP_REST_Request $request
**Since:** 5.0 | **Tags:** #Recent
Filters WP_Query arguments when querying revisions via the REST API. Serves the same purpose as the {@see 'rest_{$this->post_type}_query'} filter in WP_REST_Posts_Controller, but for the standalone WP_REST_Revisions_Controller.

### rest_themes_collection_params
**Params:** array $query_params
**Since:** 5.0 | **Tags:** #Recent
Filters REST API collection parameters for the themes controller.

### wp_rest_search_handlers
**Params:** array $search_handlers
**Since:** 5.0 | **Tags:** #Recent
Filters the search handlers to use in the REST search controller.

### rest_post_search_query
**Params:** array $query_args, WP_REST_Request $request
**Since:** 5.1 | **Tags:** #Recent
Filters the query arguments for a REST API post search request. Enables adding extra arguments or setting defaults for a post search request.

### oembed_iframe_title_attribute
**Params:** string $title, string $result, object $data, string $url
**Since:** 5.2 | **Tags:** #Recent
Filters the title attribute of the given oEmbed HTML iframe.

### rest_{$this->post_type}_item_schema
**Since:** 5.4 | **Tags:** #Variable #Recent

### rest_allowed_cors_headers
**Params:** string[] $allow_headers, WP_REST_Request $request
**Since:** 5.5 | **Tags:** #Recent
Filters the list of request headers that are allowed for REST API CORS requests. The allowed headers are passed to the browser to specify which headers can be passed to the REST API. By default, we allow the Content-* headers needed to upload files to the media endpoints. As well as the Authorization and Nonce headers for allowing authentication.

### rest_block_directory_collection_params
**Params:** array $query_params
**Since:** 5.5 | **Tags:** #Recent
Filters REST API collection parameters for the block directory controller.

### rest_exposed_cors_headers
**Params:** string[] $expose_headers, WP_REST_Request $request
**Since:** 5.5 | **Tags:** #Recent
Filters the list of response headers that are exposed to REST API CORS requests.

### rest_prepare_block_type
**Params:** WP_REST_Response $response, WP_Block_Type $block_type, WP_REST_Request $request
**Since:** 5.5 | **Tags:** #Recent
Filters a block type returned from the REST API. Allows modification of the block type data right before it is returned.

### rest_prepare_plugin
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Since:** 5.5 | **Tags:** #Recent
Filters plugin data for a REST API response.

### rest_queried_resource_route
**Params:** string $link
**Since:** 5.5 | **Tags:** #Recent
Filters the REST route for the currently queried object.

### rest_route_for_post
**Params:** string $route, WP_Post $post
**Since:** 5.5 | **Tags:** #Recent
Filters the REST API route for a post.

### rest_route_for_term
**Params:** string $route, WP_Term $term
**Since:** 5.5 | **Tags:** #Recent
Filters the REST API route for a term.

### rest_get_max_batch_size
**Params:** int $max_size
**Since:** 5.6 | **Tags:** #Recent
Filters the maximum number of REST API requests that can be included in a batch.

### rest_post_format_search_query
**Params:** array $query_args, WP_REST_Request $request
**Since:** 5.6 | **Tags:** #Recent
Filters the query arguments for a REST API post format search request. Enables adding extra arguments or setting defaults for a post format search request.

### rest_prepare_application_password
**Params:** WP_REST_Response $response, array $item, WP_REST_Request $request
**Since:** 5.6 | **Tags:** #Recent
Filters the REST API response for an application password.

### rest_pre_insert_application_password
**Params:** stdClass $prepared, WP_REST_Request $request
**Since:** 5.6 | **Tags:** #Recent
Filters an application password before it is inserted via the REST API.

### rest_term_search_query
**Params:** array $query_args, WP_REST_Request $request
**Since:** 5.6 | **Tags:** #Recent
Filters the query arguments for a REST API term search request. Enables adding extra arguments or setting defaults for a term search request.

### site_health_test_rest_capability_{$check}
**Since:** 5.6 | **Tags:** #Variable #Recent

### block_editor_rest_api_preload_paths
**Params:** WP_Block_Editor_Context $block_editor_context
**Since:** 5.8 | **Tags:** #Recent
Filters the array of REST API paths that will be used to preloaded common data for the block editor.

### rest_pattern_directory_collection_params
**Params:** array $query_params
**Since:** 5.8 | **Tags:** #Recent
Filter collection parameters for the block pattern directory controller.

### rest_prepare_block_pattern
**Params:** WP_REST_Response $response, object $raw_pattern, WP_REST_Request $request
**Since:** 5.8 | **Tags:** #Recent
Filters the REST API response for a block pattern.

### rest_prepare_sidebar
**Params:** WP_REST_Response $response, array $raw_sidebar, WP_REST_Request $request
**Since:** 5.8 | **Tags:** #Recent
Filters the REST API response for a sidebar.

### rest_prepare_widget
**Params:** WP_REST_Response|WP_Error $response, array $widget, WP_REST_Request $request
**Since:** 5.8 | **Tags:** #Recent
Filters the REST API response for a widget.

### rest_prepare_widget_type
**Params:** WP_REST_Response $response, array $widget_type, WP_REST_Request $request
**Since:** 5.8 | **Tags:** #Recent
Filters the REST API response for a widget type.

### rest_prepare_menu_location
**Params:** WP_REST_Response $response, object $location, WP_REST_Request $request
**Since:** 5.9 | **Tags:** #Recent
Filters menu location data returned from the REST API.

### rest_prepare_nav_menu_item
**Params:** WP_REST_Response $response, object $menu_item, WP_REST_Request $request
**Since:** 5.9 | **Tags:** #Recent
Filters the menu item data for a REST API response.

### rest_prepare_url_details
**Params:** WP_REST_Response $response, string $url, WP_REST_Request $request, string $remote_url_response
**Since:** 5.9 | **Tags:** #Recent
Filters the URL data for the response.

### rest_pre_insert_nav_menu_item
**Params:** object $prepared_nav_item, WP_REST_Request $request
**Since:** 5.9 | **Tags:** #Recent
Filters a menu item before it is inserted via the REST API.

### rest_route_for_post_type_items
**Params:** string $route, WP_Post_Type $post_type
**Since:** 5.9 | **Tags:** #Recent
Filters the REST API route for a post type.

### rest_route_for_taxonomy_items
**Params:** string $route, WP_Taxonomy $taxonomy
**Since:** 5.9 | **Tags:** #Recent
Filters the REST API route for a taxonomy.

### rest_url_details_cache_expiration
**Params:** int $ttl
**Since:** 5.9 | **Tags:** #Recent
Filters the cache expiration. Can be used to adjust the time until expiration in seconds for the cache of the data retrieved for the given URL.

### rest_url_details_http_request_args
**Params:** array $args, string $url
**Since:** 5.9 | **Tags:** #Recent
Filters the HTTP request args for URL data retrieval. Can be used to adjust response size limit and other WP_Http::request() args.

### rest_json_encode_options
**Params:** int $options, WP_REST_Request $request
**Since:** 6.1 | **Tags:** #Recent
Filters the JSON encoding options used to send the REST API response.

### rest_font_collections_collection_params
**Params:** array $query_params
**Since:** 6.5 | **Tags:** #Recent
Filters REST API collection parameters for the font collections controller.

### rest_prepare_font_collection
**Params:** WP_REST_Response $response, WP_Font_Collection $item, WP_REST_Request $request
**Since:** 6.5 | **Tags:** #Recent
Filters the font collection data for a REST API response.

### rest_prepare_wp_font_face
**Params:** WP_REST_Response $response, WP_Post $post, WP_REST_Request $request
**Since:** 6.5 | **Tags:** #Recent
Filters the font face data for a REST API response.

### rest_prepare_wp_font_family
**Params:** WP_REST_Response $response, WP_Post $post, WP_REST_Request $request
**Since:** 6.5 | **Tags:** #Recent
Filters the font family data for a REST API response.

### rest_wp_font_face_collection_params
**Params:** array $query_params
**Since:** 6.5 | **Tags:** #Recent
Filters collection parameters for the font face controller.

### rest_wp_font_family_collection_params
**Params:** array $query_params
**Since:** 6.5 | **Tags:** #Recent
Filters collection parameters for the font family controller.

### wp_is_rest_endpoint
**Params:** bool $is_request_endpoint
**Since:** 6.5 | **Tags:** #Recent
Filters whether a REST endpoint request is currently being handled. This may be a standalone REST API request, or an internal request dispatched from within a regular page load.

### is_post_embeddable
**Params:** bool $is_embeddable, WP_Post $post
**Since:** 6.8 | **Tags:** #Recent
Filter whether a post is embeddable.

### rest_menu_read_access
**Params:** bool $read_only_access, WP_REST_Request $request, WP_REST_Controller $controller
**Since:** 6.8 | **Tags:** #Recent
Filters whether the current user has read access to menu items via the REST API.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
