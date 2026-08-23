# WordPress Filters: User / Auth / Login / Capabilities

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### author_email
**Params:** string $comment_author_email, string $comment_id
**Since:** 1.2.1 | **Tags:** #Legacy
Filters the comment author's email for display.

### author_feed_link
**Params:** string $link, string $feed
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the feed link for a given author.

### author_link
**Params:** string $link, int $author_id, string $author_nicename
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the URL to the author's page.

### author_rewrite_rules
**Params:** string[] $author_rewrite
**Since:** 1.5.2 | **Tags:** #Legacy
Filters rewrite rules used for author archives. Likely author archives would include `/author/author-name/`, as well as pagination and feed paths for author archives.

### loginout
**Params:** string $link
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the HTML output for the Log In/Log Out link.

### pre_user_id
**Since:** 1.5.2 | **Tags:** #Legacy

### register
**Params:** string $link
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the HTML link to the Registration or Admin page. Users are sent to the admin page if logged-in, or the registration page if enabled and logged-out.

### show_password_fields
**Params:** bool $show, WP_User $profile_user
**Since:** 1.5.2 | **Tags:** #Legacy
Filters the display of the password fields.

### get_editable_authors
**Since:** 2.0 | **Tags:** #Legacy

### get_others_drafts
**Since:** 2.0 | **Tags:** #Legacy

### get_users_drafts
**Params:** string $query
**Since:** 2.0 | **Tags:** #Legacy
Filters the SQL query string for the user's drafts query.

### role_has_cap
**Params:** bool[] $capabilities, string $cap, string $name
**Since:** 2.0 | **Tags:** #Legacy
Filters which capabilities a role has.

### the_author
**Params:** string $display_name
**Since:** 2.0 | **Tags:** #Legacy
Filters the display name of the current post's author.

### user_has_cap
**Params:** bool[] $allcaps, string[] $caps, array $args, WP_User $user
**Since:** 2.0 | **Tags:** #Legacy
Dynamically filter a user's capabilities.

### pre_user_description
**Since:** 2.0.11 | **Tags:** #Legacy

### pre_user_display_name
**Params:** string $display_name
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a user's display name before the user is created or updated.

### pre_user_email
**Params:** string $raw_user_email
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a user's email before the user is created or updated.

### pre_user_first_name
**Since:** 2.0.11 | **Tags:** #Legacy

### pre_user_last_name
**Since:** 2.0.11 | **Tags:** #Legacy

### pre_user_login
**Params:** string $sanitized_user_login
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a username after it has been sanitized. This filter is called before the user is created or updated.

### pre_user_nicename
**Params:** string $user_nicename
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a user's nicename before the user is created or updated.

### pre_user_nickname
**Since:** 2.0.11 | **Tags:** #Legacy

### pre_user_url
**Params:** string $raw_user_url
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a user's URL before the user is created or updated.

### sanitize_user
**Params:** string $username, string $raw_username, bool $strict
**Since:** 2.0.11 | **Tags:** #Legacy
Filters a sanitized username string.

### validate_username
**Params:** bool $valid, string $username
**Since:** 2.0.11 | **Tags:** #Legacy
Filters whether the provided username is valid.

### login_errors
**Params:** string $errors
**Since:** 2.1 | **Tags:** #Legacy
Filters the error messages displayed above the login form.

### login_headerurl
**Params:** string $login_header_url
**Since:** 2.1 | **Tags:** #Legacy
Filters link URL of the header logo above login form.

### login_message
**Params:** string $message
**Since:** 2.1 | **Tags:** #Legacy
Filters the message to display above the login form.

### registration_errors
**Params:** WP_Error $errors, string $sanitized_user_login, string $user_email
**Since:** 2.1 | **Tags:** #Legacy
Filters the errors encountered when a new user is being registered. The filtered WP_Error object may, for example, contain errors for an invalid or existing username or email address. A WP_Error object should always be returned, but may or may not contain errors. If any errors are present in $errors, this will abort the user's registration.

### user_can_richedit
**Params:** bool $wp_rich_edit
**Since:** 2.1 | **Tags:** #Legacy
Filters whether the user can access the visual editor.

### user_registration_email
**Params:** string $user_email
**Since:** 2.1 | **Tags:** #Legacy
Filters the email address of a user being registered.

### user_trailingslashit
**Params:** string $url, string $type_of_url
**Since:** 2.2 | **Tags:** #Legacy
Filters the trailing-slashed string, depending on whether the site is set to use trailing slashes.

### auth_cookie
**Params:** string $cookie, int $user_id, int $expiration, string $scheme, string $token
**Since:** 2.5 | **Tags:** #Legacy
Filters the authentication cookie.

### check_password
**Params:** bool $check, string $password, string $hash, string|int $user_id
**Since:** 2.5 | **Tags:** #Legacy
Filters whether the plaintext password matches the hashed password.

### get_user_option_{$option}
**Since:** 2.5 | **Tags:** #Variable #Legacy

### login_messages
**Params:** string $messages
**Since:** 2.5 | **Tags:** #Legacy
Filters instructional messages displayed above the login form.

### nonce_life
**Params:** int $lifespan, string|int $action
**Since:** 2.5 | **Tags:** #Legacy
Filters the lifespan of nonces in seconds.

### wp_authenticate_user
**Params:** WP_User|WP_Error $user, string $password
**Since:** 2.5 | **Tags:** #Legacy
Filters whether the given user can be authenticated with the provided password.

### editable_slug
**Params:** string $slug, WP_Term|WP_Post $tag
**Since:** 2.6 | **Tags:** #Legacy
Filters the editable slug for a post or term. Note: This is a multi-use hook in that it is leveraged both for editable post URIs and term slugs.

### allow_password_reset
**Params:** bool $allow, int $user_id
**Since:** 2.7 | **Tags:** #Legacy
Filters whether to allow a password to be reset.

### get_usernumposts
**Params:** string $count, int $userid, string|array $post_type, bool $public_only
**Since:** 2.7 | **Tags:** #Legacy
Filters the number of posts a user has written.

### login_redirect
**Params:** string $redirect_to, string $requested_redirect_to, WP_User|WP_Error $user
**Since:** 2.7 | **Tags:** #Legacy
Filters the login redirect URL.

### additional_capabilities_display
**Params:** bool $enable, WP_User $profile_user
**Since:** 2.8 | **Tags:** #Legacy
Filters whether to display additional capabilities for the user. The 'Additional Capabilities' section will only be enabled if the number of the user's capabilities exceeds their number of roles.

### authenticate
**Params:** null|WP_User|WP_Error $user, string $username, string $password
**Since:** 2.8 | **Tags:** #Legacy
Filters whether a set of user login credentials are valid. A WP_User object is returned if the credentials authenticate a user. WP_Error or null otherwise.

### auth_cookie_expiration
**Params:** int $length, int $user_id, bool $remember
**Since:** 2.8 | **Tags:** #Legacy
Filters the duration of the authentication cookie expiration period.

### editable_extensions
**Params:** string[] $default_types, string $plugin
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of file types allowed for editing in the plugin file editor.

### editable_roles
**Params:** array[] $all_roles
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of editable roles.

### get_the_author_{$field}
**Since:** 2.8 | **Tags:** #Variable #Legacy

### is_email
**Params:** string|false $is_email, string $email, string $context
**Since:** 2.8 | **Tags:** #Legacy
Filters whether an email address is valid. This filter is evaluated under several different contexts, such as 'email_too_short', 'email_no_at', 'local_invalid_chars', 'domain_period_sequence', 'domain_period_limits', 'domain_no_periods', 'sub_hyphen_limits', 'sub_invalid_chars', or no specific context.

### login_url
**Params:** string $login_url, string $redirect, bool $force_reauth
**Since:** 2.8 | **Tags:** #Legacy
Filters the login URL.

### logout_url
**Params:** string $logout_url, string $redirect
**Since:** 2.8 | **Tags:** #Legacy
Filters the logout URL.

### lostpassword_url
**Params:** string $lostpassword_url, string $redirect
**Since:** 2.8 | **Tags:** #Legacy
Filters the Lost Password URL.

### map_meta_cap
**Params:** string[] $caps, string $cap, int $user_id, array $args
**Since:** 2.8 | **Tags:** #Legacy
Filters the primitive capabilities required of the given user to satisfy the capability being checked.

### retrieve_password_message
**Params:** string $message, string $key, string $user_login, WP_User $user_data
**Since:** 2.8 | **Tags:** #Legacy
Filters the message body of the password reset mail. If the filtered message is empty, the password reset email will not be sent.

### retrieve_password_title
**Params:** string $title, string $user_login, WP_User $user_data
**Since:** 2.8 | **Tags:** #Legacy
Filters the subject of the password reset email.

### the_author_{$field}
**Since:** 2.8 | **Tags:** #Variable #Legacy

### the_modified_author
**Params:** string $display_name
**Since:** 2.8 | **Tags:** #Legacy
Filters the display name of the author who last edited the current post.

### user_row_actions
**Params:** string[] $actions, WP_User $user_object
**Since:** 2.8 | **Tags:** #Legacy
Filters the action links displayed under each user in the Users list table.

### auth_redirect_scheme
**Params:** string $scheme
**Since:** 2.9 | **Tags:** #Legacy
Filters the authentication redirect scheme.

### edit_user_{$field}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### pre_user_{$field}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### the_author_posts_link
**Params:** string $link, string $author, string $title
**Since:** 2.9 | **Tags:** #Legacy
Filters the link to the author page of the author of the current post.

### user_contactmethods
**Params:** string[] $methods, WP_User|null $user
**Since:** 2.9 | **Tags:** #Legacy
Filters the user contact methods.

### user_{$field}
**Since:** 2.9 | **Tags:** #Variable #Legacy

### user_{$name}_label
**Since:** 2.9 | **Tags:** #Variable #Legacy

### enable_edit_any_user_configuration
**Since:** 3.0 | **Tags:** #Modern

### enable_post_by_email_configuration
**Params:** bool $enabled
**Since:** 3.0 | **Tags:** #Modern
Filters whether the post-by-email functionality is enabled.

### get_blogs_of_user
**Params:** object[] $sites, int $user_id, bool $all
**Since:** 3.0 | **Tags:** #Modern
Filters the list of sites a user belongs to.

### login_form_bottom
**Params:** string $content, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters content to display at the bottom of the login form. The filter evaluates just preceding the closing form tag element.

### login_form_defaults
**Params:** array $defaults
**Since:** 3.0 | **Tags:** #Modern
Filters the default login form output arguments.

### login_form_middle
**Params:** string $content, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters content to display in the middle of the login form. The filter evaluates just following the location where the 'login-password' field is displayed.

### login_form_top
**Params:** string $content, array $args
**Since:** 3.0 | **Tags:** #Modern
Filters content to display at the top of the login form. The filter evaluates just following the opening form tag element.

### lostpassword_redirect
**Params:** string $lostpassword_redirect
**Since:** 3.0 | **Tags:** #Modern
Filters the URL redirected to after submitting the lostpassword/retrievepassword form.

### random_password
**Params:** string $password, int $length, bool $special_chars, bool $extra_special_chars
**Since:** 3.0 | **Tags:** #Modern
Filters the randomly-generated password.

### registration_redirect
**Params:** string $registration_redirect, int|WP_Error $errors
**Since:** 3.0 | **Tags:** #Modern
Filters the registration redirect URL.

### shake_error_codes
**Params:** string[] $shake_error_codes
**Since:** 3.0 | **Tags:** #Modern
Filters the error codes array for shaking the login form.

### edit_profile_url
**Params:** string $url, int $user_id, string $scheme
**Since:** 3.1 | **Tags:** #Modern
Filters the URL for a user's profile editor.

### secure_auth_cookie
**Params:** bool $secure, int $user_id
**Since:** 3.1 | **Tags:** #Modern
Filters whether the auth cookie should only be sent over HTTPS.

### secure_auth_redirect
**Params:** bool $secure
**Since:** 3.1 | **Tags:** #Modern
Filters whether to use a secure authentication redirect.

### secure_logged_in_cookie
**Params:** bool $secure_logged_in_cookie, int $user_id, bool $secure
**Since:** 3.1 | **Tags:** #Modern
Filters whether the logged in cookie should only be sent over HTTPS.

### secure_signon_cookie
**Params:** bool $secure_cookie, array $credentials
**Since:** 3.1 | **Tags:** #Modern
Filters whether to use a secure sign-on cookie.

### show_admin_bar
**Params:** bool $show_admin_bar
**Since:** 3.1 | **Tags:** #Modern
Filters whether to show the admin bar. Returning false to this hook is the recommended way to hide the admin bar. The user's display preference is used for logged in users.

### user_admin_url
**Params:** string $url, string $path, string|null $scheme
**Since:** 3.1 | **Tags:** #Modern
Filters the user admin URL for the current user.

### user_dashboard_url
**Params:** string $url, int $user_id, string $path, string $scheme
**Since:** 3.1 | **Tags:** #Modern
Filters the dashboard URL for a user.

### found_users_query
**Params:** string $sql, WP_User_Query $query
**Since:** 3.2 | **Tags:** #Modern
Filters SELECT FOUND_ROWS() query for the current WP_User_Query instance.

### redirect_user_admin_request
**Params:** bool $redirect_user_admin_request
**Since:** 3.2 | **Tags:** #Modern
Filters whether to redirect the request to the User Admin in Multisite.

### is_multi_author
**Params:** bool $is_multi_author
**Since:** 3.3 | **Tags:** #Modern
Filters whether the site has more than one author with published posts.

### autocomplete_users_for_site_admins
**Since:** 3.4 | **Tags:** #Modern

### get_edit_user_link
**Params:** string $link, int $user_id
**Since:** 3.5 | **Tags:** #Modern
Filters the user edit link.

### login_body_class
**Params:** string[] $classes, string $action
**Since:** 3.5 | **Tags:** #Modern
Filters the login page body classes.

### nonce_user_logged_out
**Params:** int $uid, string|int $action
**Since:** 3.5 | **Tags:** #Modern
Filters whether the user who generated the nonce is logged out.

### register_url
**Params:** string $register
**Since:** 3.6 | **Tags:** #Modern
Filters the user registration URL.

### user_search_columns
**Params:** string[] $search_columns, string $search, WP_User_Query $query
**Since:** 3.6 | **Tags:** #Modern
Filters the columns to search in a WP_User_Query search. The default columns depend on the search term, and include 'ID', 'user_login', 'user_email', 'user_url', 'user_nicename', and 'display_name'.

### check_is_user_spammed
**Params:** bool $spammed, WP_User $user
**Since:** 3.7 | **Tags:** #Modern
Filters whether the user has been marked as a spammer.

### password_reset_key_expired
**Params:** WP_Error $return, int $user_id
**Since:** 3.7 | **Tags:** #Modern
Filters the return value of check_password_reset_key() when an old-style key or an expired key is used. Prior to 3.7, plain-text keys were stored in the database.

### determine_current_user
**Params:** int|false $user_id
**Since:** 3.9 | **Tags:** #Modern
Filters the current user. The default filters use this to determine the current user from the request's cookies, if available. Returning a value of false will effectively short-circuit setting the current user.

### password_hint
**Params:** string $hint
**Since:** 4.1 | **Tags:** #Modern
Filters the text describing the site's password complexity policy.

### logout_redirect
**Params:** string $redirect_to, string $requested_redirect_to, WP_User $user
**Since:** 4.2 | **Tags:** #Modern
Filters the log out redirect URL.

### email_change_email
**Params:** array $email_change_email, array $user, array $userdata
**Since:** 4.3 | **Tags:** #Modern
Filters the contents of the email sent when the user's email is changed.

### password_change_email
**Params:** array $pass_change_email, array $user, array $userdata
**Since:** 4.3 | **Tags:** #Modern
Filters the contents of the email sent when the user's password is changed.

### password_reset_expiration
**Params:** int $expiration
**Since:** 4.3 | **Tags:** #Modern
Filters the expiration time of password reset keys.

### send_email_change_email
**Params:** bool $send, array $user, array $userdata
**Since:** 4.3 | **Tags:** #Modern
Filters whether to send the email change email.

### send_password_change_email
**Params:** bool $send, array $user, array $userdata
**Since:** 4.3 | **Tags:** #Modern
Filters whether to send the password change email.

### get_role_list
**Params:** string[] $role_list, WP_User $user_object
**Since:** 4.4 | **Tags:** #Modern
Filters the returned array of translated role names for a user.

### illegal_user_logins
**Params:** array $usernames
**Since:** 4.4 | **Tags:** #Modern
Filters the list of disallowed usernames.

### insert_user_meta
**Params:** array $meta, WP_User $user, bool $update, array $userdata
**Since:** 4.4 | **Tags:** #Modern
Filters a user's meta values and keys immediately after the user is created or updated and before any user meta is inserted or updated. Does not include contact methods. These are added using `wp_get_user_contact_methods( $user )`. For custom meta fields, see the {@see 'insert_custom_user_meta'} filter.

### register_post_type_args
**Params:** array $args, string $post_type
**Since:** 4.4 | **Tags:** #Modern
Filters the arguments for registering a post type.

### register_taxonomy_args
**Params:** array $args, string $taxonomy, string[] $object_type
**Since:** 4.4 | **Tags:** #Modern
Filters the arguments for registering a taxonomy.

### user_profile_picture_description
**Params:** string $description, WP_User $profile_user
**Since:** 4.4 | **Tags:** #Modern
Filters the user profile picture description displayed under the Gravatar.

### register_meta_args
**Params:** array $args, array $defaults, string $object_type, string $meta_key
**Since:** 4.6 | **Tags:** #Modern
Filters the registration arguments when registering meta.

### auth_{$object_type}_meta_{$meta_key}
**Since:** 4.7 | **Tags:** #Variable #Modern

### register_setting_args
**Params:** array $args, array $defaults, string $option_group, string $option_name
**Since:** 4.7 | **Tags:** #Modern
Filters the registration arguments when registering a setting.

### login_link_separator
**Params:** string $login_link_separator
**Since:** 4.9 | **Tags:** #Modern
Filters the separator used between login form navigation links.

### login_title
**Params:** string $login_title, string $title
**Since:** 4.9 | **Tags:** #Modern
Filters the title tag content for login page.

### username_exists
**Params:** int|false $user_id, string $username
**Since:** 4.9 | **Tags:** #Modern
Filters whether the given username exists.

### auth_{$object_type}_meta_{$meta_key}_for_{$object_subtype}
**Since:** 5.0 | **Tags:** #Variable #Recent

### user_erasure_fulfillment_email_to
**Params:** string $user_email, WP_User_Request $request
**Since:** 5.0 | **Tags:** #Recent
Filters the recipient of the data erasure fulfillment notification.

### user_request_action_confirmed_message
**Params:** string $message, int $request_id
**Since:** 5.0 | **Tags:** #Recent
Filters the message displayed to a user when they confirm a data request.

### user_request_action_description
**Params:** string $description, string $action_name
**Since:** 5.0 | **Tags:** #Recent
Filters the user action description.

### user_request_action_email_content
**Params:** string $content, array $email_data
**Since:** 5.0 | **Tags:** #Recent
Filters the text of the email sent when an account action is attempted. The following strings have a special meaning and will get replaced dynamically: - `###DESCRIPTION###` Description of the action being performed so the user knows what the email is for. - `###CONFIRM_URL###` The link to click on to confirm the account action. - `###SITENAME###`    The name of the site. - `###SITEURL###`     The URL to the site.

### user_request_action_email_subject
**Params:** string $subject, string $sitename, array $email_data
**Since:** 5.0 | **Tags:** #Recent
Filters the subject of the email sent when an account action is attempted.

### user_request_confirmed_email_subject
**Params:** string $subject, string $sitename, array $email_data
**Since:** 5.0 | **Tags:** #Recent
Filters the subject of the user request confirmation email.

### user_request_confirmed_email_to
**Params:** string $admin_email, WP_User_Request $request
**Since:** 5.0 | **Tags:** #Recent
Filters the recipient of the data request confirmation notification. In a Multisite environment, this will default to the email address of the network admin because, by default, single site admins do not have the capabilities required to process requests. Some networks may wish to delegate those capabilities to a single-site admin, or a dedicated person responsible for managing privacy requests.

### user_request_key_expiration
**Params:** int $expiration
**Since:** 5.0 | **Tags:** #Recent
Filters the expiration time of confirm keys.

### pre_count_users
**Params:** null|array $result, string $strategy, int $site_id
**Since:** 5.1 | **Tags:** #Recent
Filters the user count before queries are run. Return a non-null value to cause count_users() to return early.

### users_pre_query
**Since:** 5.1 | **Tags:** #Recent

### login_headertext
**Params:** string $login_header_text
**Since:** 5.2 | **Tags:** #Recent
Filters the link text of the header logo above the login form.

### users_have_additional_content
**Params:** bool $users_have_additional_content, int[] $user_ids
**Since:** 5.2 | **Tags:** #Recent
Filters whether the users being deleted have additional content associated with them outside of the `post_author` and `link_owner` relationships.

### insert_with_markers_inline_instructions
**Params:** string[] $instructions, string $marker
**Since:** 5.3 | **Tags:** #Recent
Filters the inline instructions inserted before the dynamically generated content.

### register_sidebar_defaults
**Params:** array $defaults
**Since:** 5.3 | **Tags:** #Recent
Filters the sidebar default arguments.

### user_request_action_email_headers
**Params:** string|array $headers, string $subject, string $content, int $request_id, array $email_data
**Since:** 5.4 | **Tags:** #Recent
Filters the headers of the email sent when an account action is attempted.

### user_request_confirmed_email_headers
**Params:** string|array $headers, string $subject, string $content, int $request_id, array $email_data
**Since:** 5.4 | **Tags:** #Recent
Filters the headers of the user request confirmation email.

### lostpassword_errors
**Params:** WP_Error $errors, WP_User|false $user_data
**Since:** 5.5 | **Tags:** #Recent
Filters the errors encountered on a password reset request. The filtered WP_Error object may, for example, contain errors for an invalid username or email address. A WP_Error object should always be returned, but may or may not contain errors. If any errors are present in $errors, this will abort the password reset request.

### register_block_type_args
**Params:** array $args, string $block_type
**Since:** 5.5 | **Tags:** #Recent
Filters the arguments for registering a block type.

### application_password_is_api_request
**Params:** bool $is_api_request
**Since:** 5.6 | **Tags:** #Recent
Filters whether this is an API request that Application Passwords can be used on. By default, Application Passwords is available for the REST API and XML-RPC.

### email_exists
**Params:** int|false $user_id, string $email
**Since:** 5.6 | **Tags:** #Recent
Filters whether the given email exists.

### invited_user_email
**Params:** array $new_user_email, int $user_id, array $role, string $newuser_key
**Since:** 5.6 | **Tags:** #Recent
Filters the contents of the email sent when an existing user is invited to join the site.

### login_site_html_link
**Params:** string $link
**Since:** 5.7 | **Tags:** #Recent
Filters the "Go to site" link displayed in the login page footer.

### lostpassword_user_data
**Params:** WP_User|false $user_data, WP_Error $errors
**Since:** 5.7 | **Tags:** #Recent
Filters the user data during a password reset request. Allows, for example, custom validation using data other than username or email address.

### user_erasure_fulfillment_email_content
**Params:** string $content, array $email_data
**Since:** 5.8 | **Tags:** #Recent
Filters the body of the data erasure fulfillment notification. The email is sent to a user when their data erasure request is fulfilled by an administrator. The following strings have a special meaning and will get replaced dynamically: - `###SITENAME###`           The name of the site. - `###PRIVACY_POLICY_URL###` Privacy policy page URL. - `###SITEURL###`            The URL to the site.

### user_erasure_fulfillment_email_headers
**Params:** string|array $headers, string $subject, string $content, int $request_id, array $email_data
**Since:** 5.8 | **Tags:** #Recent
Filters the headers of the data erasure fulfillment notification.

### user_erasure_fulfillment_email_subject
**Params:** string $subject, string $sitename, array $email_data
**Since:** 5.8 | **Tags:** #Recent
Filters the subject of the email sent when an erasure request is completed.

### user_request_confirmed_email_content
**Params:** string $content, array $email_data
**Since:** 5.8 | **Tags:** #Recent
Filters the body of the user request confirmation email. The email is sent to an administrator when a user request is confirmed. The following strings have a special meaning and will get replaced dynamically: - `###SITENAME###`    The name of the site. - `###USER_EMAIL###`  The user email for the request. - `###DESCRIPTION###` Description of the action being performed so the user knows what the email is for. - `###MANAGE_URL###`  The URL to manage requests. - `###SITEURL###`     The URL to the site.

### insert_custom_user_meta
**Params:** array $custom_meta, WP_User $user, bool $update, array $userdata
**Since:** 5.9 | **Tags:** #Recent
Filters a user's custom meta values and keys immediately after the user is created or updated and before any user meta is inserted or updated. For non-custom meta fields, see the {@see 'insert_user_meta'} filter.

### login_display_language_dropdown
**Params:** bool $display
**Since:** 5.9 | **Tags:** #Recent
Filters whether to display the Language selector on the login screen.

### login_language_dropdown_args
**Params:** array $args
**Since:** 5.9 | **Tags:** #Recent
Filters default arguments for the Language select input on the login screen. The arguments get passed to the wp_dropdown_languages() function.

### register_{$post_type}_post_type_args
**Since:** 6.0 | **Tags:** #Variable #Recent

### register_{$taxonomy}_taxonomy_args
**Since:** 6.0 | **Tags:** #Variable #Recent

### retrieve_password_notification_email
**Params:** array $defaults, string $key, string $user_login, WP_User $user_data
**Since:** 6.0 | **Tags:** #Recent
Filters the contents of the reset password notification email sent to the user.

### send_retrieve_password_email
**Params:** bool $send, string $user_login, WP_User $user_data
**Since:** 6.0 | **Tags:** #Recent
Filters whether to send the retrieve password email. Return false to disable sending the email.

### the_author_link
**Params:** string $link, string $author_url, WP_User $authordata
**Since:** 6.0 | **Tags:** #Recent
Filters the author URL link HTML.

### lost_password_html_link
**Params:** string $html_link
**Since:** 6.1 | **Tags:** #Recent
Filters the link that allows the user to reset the lost password.

### new_admin_email_subject
**Params:** string $subject
**Since:** 6.5 | **Tags:** #Recent
Filters the subject of the email sent when a change of site admin email address is attempted.

### password_needs_rehash
**Params:** bool $needs_rehash, string $hash, string|int $user_id
**Since:** 6.8 | **Tags:** #Recent
Filters whether the password hash needs to be rehashed.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
