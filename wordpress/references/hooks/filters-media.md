# WordPress Filters: Media / Uploads / Images / Attachments

> Core filter hooks, organized by functional category. Sourced from WordPress core docblocks (wp-includes / wp-admin).
> Tags: #Legacy = superseded API kept for backward compatibility · #deprecated = do not use in new code · others are current.

---

### attachment_icon
**Since:** 2.0 | **Tags:** #Legacy

### attachment_innerHTML
**Since:** 2.0 | **Tags:** #Legacy

### attachment_link
**Params:** string $link, int $post_id
**Since:** 2.0 | **Tags:** #Legacy
Filters the permalink for an attachment.

### attachment_max_dims
**Since:** 2.0 | **Tags:** #Legacy

### icon_dir
**Params:** string $path
**Since:** 2.0 | **Tags:** #Legacy
Filters the icon directory path.

### icon_dir_uri
**Params:** string $uri
**Since:** 2.0 | **Tags:** #Legacy
Filters the icon directory URI.

### prepend_attachment
**Params:** string $p
**Since:** 2.0 | **Tags:** #Legacy
Filters the attachment markup to be prepended to the post content.

### upload_dir
**Params:** array $uploads
**Since:** 2.0 | **Tags:** #Legacy
Filters the uploads directory data.

### upload_mimes
**Params:** array $t, int|WP_User|null $user
**Since:** 2.0 | **Tags:** #Legacy
Filters the list of allowed mime types and file extensions.

### get_attached_file
**Params:** string|false $file, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attached file based on the given ID.

### pre_upload_error
**Params:** bool $error
**Since:** 2.1 | **Tags:** #Legacy
Filters whether to preempt the XML-RPC media upload. Returning a truthy value will effectively short-circuit the media upload, returning that value as a 500 error instead.

### update_attached_file
**Params:** string $file, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the path to the attached file to update.

### wp_create_file_in_uploads
**Params:** string $file, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attachment file path after the custom header or background image is set. Used for file replication.

### wp_create_thumbnail
**Since:** 2.1 | **Tags:** #Legacy

### wp_delete_file
**Params:** string $file
**Since:** 2.1 | **Tags:** #Legacy
Filters the path of the file to delete.

### wp_generate_attachment_metadata
**Params:** array $metadata, int $attachment_id, string $context
**Since:** 2.1 | **Tags:** #Legacy
Filters the generated attachment meta data.

### wp_get_attachment_metadata
**Params:** array $data, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attachment meta data.

### wp_get_attachment_thumb_file
**Params:** string $thumbfile, int $post_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attachment thumbnail file path.

### wp_get_attachment_thumb_url
**Params:** string $thumbnail_url, int $post_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attachment thumbnail URL.

### wp_get_attachment_url
**Params:** string $url, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the attachment URL.

### wp_handle_upload
**Params:** array $upload, string $context
**Since:** 2.1 | **Tags:** #Legacy
Filters the data array for the uploaded file.

### wp_mime_type_icon
**Params:** string $icon, string $mime, int $post_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the mime type icon.

### wp_update_attachment_metadata
**Params:** array $data, int $attachment_id
**Since:** 2.1 | **Tags:** #Legacy
Filters the updated attachment meta data.

### attachment_fields_to_edit
**Params:** array $form_fields, WP_Post $post
**Since:** 2.5 | **Tags:** #Legacy
Filters the attachment fields to edit.

### attachment_fields_to_save
**Params:** array $post, array $attachment
**Since:** 2.5 | **Tags:** #Legacy
Filters the attachment fields to be saved.

### editor_max_image_size
**Params:** int[] $max_image_size, string|int[] $size, string $context
**Since:** 2.5 | **Tags:** #Legacy
Filters the maximum image size dimensions for the editor.

### ext2type
**Params:** array[] $ext2type
**Since:** 2.5 | **Tags:** #Legacy
Filters file type based on the extension name.

### file_is_displayable_image
**Params:** bool $result, string $path
**Since:** 2.5 | **Tags:** #Legacy
Filters whether the current image is displayable in the browser.

### gallery_style
**Params:** string $gallery_style
**Since:** 2.5 | **Tags:** #Legacy
Filters the default gallery shortcode CSS styles.

### icon_dirs
**Params:** string[] $uris
**Since:** 2.5 | **Tags:** #Legacy
Filters the array of icon directory URIs.

### image_downsize
**Params:** bool|array $downsize, int $id, string|int[] $size
**Since:** 2.5 | **Tags:** #Legacy
Filters whether to preempt the output of image_downsize(). Returning a truthy value from the filter will effectively short-circuit down-sizing the image, returning that value instead.

### image_send_to_editor
**Params:** string $html, int $id, string $caption, string $title, string $align, string $url, string|int[] $size, string $alt, string $rel
**Since:** 2.5 | **Tags:** #Legacy
Filters the image HTML markup to send to the editor when inserting an image.

### intermediate_image_sizes
**Params:** string[] $default_sizes
**Since:** 2.5 | **Tags:** #Legacy
Filters the list of intermediate image sizes.

### jpeg_quality
**Params:** int $quality, string $context
**Since:** 2.5 | **Tags:** #Legacy
Filters the JPEG compression quality for backward-compatibility. Applies only during initial editor instantiation, or when set_quality() is run manually without the `$quality` argument. The WP_Image_Editor::set_quality() method has priority over the filter. The filter is evaluated under two contexts: 'image_resize', and 'edit_image', (when a JPEG image is saved to file).

### media_meta
**Params:** string $media_dims, WP_Post $post
**Since:** 2.5 | **Tags:** #Legacy
Filters the media metadata.

### media_send_to_editor
**Params:** string $html, int $send_id, array $attachment
**Since:** 2.5 | **Tags:** #Legacy
Filters the HTML markup for a media item sent to the editor.

### media_upload_default_tab
**Params:** string $tab
**Since:** 2.5 | **Tags:** #Legacy
Filters the default tab in the legacy (pre-3.5.0) media popup.

### media_upload_default_type
**Params:** string $type
**Since:** 2.5 | **Tags:** #Legacy
Filters the default media upload type in the legacy (pre-3.5.0) media popup.

### media_upload_tabs
**Params:** string[] $_default_tabs
**Since:** 2.5 | **Tags:** #Legacy
Filters the available tabs in the legacy (pre-3.5.0) media popup.

### post_gallery
**Params:** string $output, array $attr, int $instance
**Since:** 2.5 | **Tags:** #Legacy
Filters the default gallery shortcode output. If the filtered output isn't empty, it will be used instead of generating the default gallery template.

### post_mime_types
**Params:** array $post_mime_types
**Since:** 2.5 | **Tags:** #Legacy
Filters the default list of post mime types.

### upload_size_limit
**Params:** int $size, int $u_bytes, int $p_bytes
**Since:** 2.5 | **Tags:** #Legacy
Filters the maximum upload size allowed in php.ini.

### wp_read_image_metadata
**Params:** array $meta, string $file, int $image_type, array $iptc, array $exif
**Since:** 2.5 | **Tags:** #Legacy
Filters the array of meta data read from an image's exif data.

### wp_read_image_metadata_types
**Params:** int[] $image_types
**Since:** 2.5 | **Tags:** #Legacy
Filters the image types to check for exif data.

### get_image_tag
**Params:** string $html, int $id, string $alt, string $title, string $align, string|int[] $size
**Since:** 2.6 | **Tags:** #Legacy
Filters the HTML content for the image tag.

### get_image_tag_class
**Params:** string $class, int $id, string $align, string|int[] $size
**Since:** 2.6 | **Tags:** #Legacy
Filters the value of the attachment's image tag class attribute.

### image_add_caption_shortcode
**Params:** string $shcode, string $html
**Since:** 2.6 | **Tags:** #Legacy
Filters the image HTML markup including the caption shortcode.

### image_make_intermediate_size
**Since:** 2.6 | **Tags:** #Legacy

### img_caption_shortcode
**Params:** string $output, array $attr, string $content
**Since:** 2.6 | **Tags:** #Legacy
Filters the default caption shortcode output. If the filtered output isn't empty, it will be used instead of generating the default caption template.

### media_upload_form_url
**Params:** string $form_action_url, string $type
**Since:** 2.6 | **Tags:** #Legacy
Filters the media upload form action URL.

### wp_get_attachment_link
**Params:** string $link_html, int|WP_Post $post, string|int[] $size, bool $permalink, bool $icon, string|false $text, array|string $attr
**Since:** 2.7 | **Tags:** #Legacy
Filters a retrieved attachment page link.

### image_send_to_editor_url
**Params:** string $html, string $src, string $alt, string $align
**Since:** 2.8 | **Tags:** #Legacy
Filters the image URL sent to the editor.

### media_row_actions
**Params:** string[] $actions, WP_Post $post, bool $detached
**Since:** 2.8 | **Tags:** #Legacy
Filters the action links for each attachment in the Media list table.

### wp_feed_cache_transient_lifetime
**Params:** int $lifetime, string $name
**Since:** 2.8 | **Tags:** #Legacy
Filters the transient lifetime of the feed cache.

### wp_get_attachment_image_attributes
**Params:** string[] $attr, WP_Post $attachment, string|int[] $size
**Since:** 2.8 | **Tags:** #Legacy
Filters the list of attachment image attributes.

### intermediate_image_sizes_advanced
**Params:** array $new_sizes, array $image_meta, int $attachment_id
**Since:** 2.9 | **Tags:** #Legacy
Filters the image sizes automatically generated when uploading an image.

### load_image_to_edit
**Params:** resource|GdImage $image, int $attachment_id, string|int[] $size
**Since:** 2.9 | **Tags:** #Legacy
Filters the current image being loaded for editing.

### load_image_to_edit_path
**Params:** string|false $filepath, int $attachment_id, string|int[] $size
**Since:** 2.9 | **Tags:** #Legacy
Filters the returned path or URL of the current image.

### post_thumbnail_html
**Params:** string $html, int $post_id, int $post_thumbnail_id, string|int[] $size, string|array $attr
**Since:** 2.9 | **Tags:** #Legacy
Filters the post thumbnail HTML.

### post_thumbnail_size
**Params:** string|int[] $size, int $post_id
**Since:** 2.9 | **Tags:** #Legacy
Filters the post thumbnail size.

### upload_per_page
**Since:** 2.9 | **Tags:** #Legacy

### _wp_relative_upload_path
**Params:** string $new_path, string $path
**Since:** 2.9 | **Tags:** #Legacy
Filters the relative path to an uploaded file.

### getimagesize_mimes_to_exts
**Params:** array $mime_to_ext
**Since:** 3.0 | **Tags:** #Modern
Filters the list mapping image mime types to their respective extensions.

### unzip_file_use_ziparchive
**Since:** 3.0 | **Tags:** #Modern

### wp_check_filetype_and_ext
**Params:** array $wp_check_filetype_and_ext, string $file, string $filename, string[]|null $mimes, string|false $real_mime
**Since:** 3.0 | **Tags:** #Modern
Filters the "real" file type of the given file.

### wp_upload_bits
**Params:** array|string $upload_bits_error
**Since:** 3.0 | **Tags:** #Modern
Filters whether to treat the upload bits as an error. Returning a non-array from the filter will effectively short-circuit preparing the upload bits and return that value instead. An error message should be returned as a string.

### get_media_item_args
**Params:** array $parsed_args
**Since:** 3.1 | **Tags:** #Modern
Filters the arguments used to retrieve an image for the edit image form.

### load_image_to_edit_attachmenturl
**Params:** string|false $image_url, int $attachment_id, string|int[] $size
**Since:** 3.1 | **Tags:** #Modern
Filters the path to an attachment's URL when editing the image. The filter is only evaluated if the file isn't stored locally and `allow_url_fopen` is enabled on the server.

### load_image_to_edit_filesystempath
**Params:** string $path, int $attachment_id, string|int[] $size
**Since:** 3.1 | **Tags:** #Modern
Filters the path to an attachment's file when editing the image. The filter is evaluated for all image sizes except 'full'.

### media_upload_mime_type_links
**Since:** 3.1 | **Tags:** #Modern

### use_default_gallery_style
**Params:** bool $print
**Since:** 3.1 | **Tags:** #Modern
Filters whether to print default gallery styles.

### display_media_states
**Params:** string[] $media_states, WP_Post $post
**Since:** 3.2 | **Tags:** #Modern
Filters the default media display states for items in the Media list table.

### image_memory_limit
**Params:** int|string $filtered_limit
**Since:** 3.2 | **Tags:** #Modern
Filters the memory limit allocated for image manipulation.

### image_size_names_choose
**Params:** string[] $size_names
**Since:** 3.3 | **Tags:** #Modern
Filters the names and labels of the default image sizes.

### plupload_init
**Params:** array $plupload_init
**Since:** 3.3 | **Tags:** #Modern
Filters the default Plupload settings.

### type_url_form_media
**Params:** string $form_html
**Since:** 3.3 | **Tags:** #Modern
Filters the insert media from URL form HTML.

### upload_post_params
**Params:** array $post_params
**Since:** 3.3 | **Tags:** #Modern
Filters the media upload post parameters.

### image_resize_dimensions
**Params:** null|mixed $null, int $orig_w, int $orig_h, int $dest_w, int $dest_h, bool|array $crop
**Since:** 3.4 | **Tags:** #Modern
Filters whether to preempt calculating the image resize dimensions. Returning a non-null value from the filter will effectively short-circuit image_resize_dimensions(), returning that value instead.

### plupload_default_params
**Params:** array $params
**Since:** 3.4 | **Tags:** #Modern
Filters the Plupload default parameters.

### plupload_default_settings
**Params:** array $defaults
**Since:** 3.4 | **Tags:** #Modern
Filters the Plupload default settings.

### wp_cache_themes_persistently
**Params:** bool $cache_expiration, string $context
**Since:** 3.4 | **Tags:** #Modern
Filters whether to get the cache of the registered theme directories.

### image_editor_default_mime_type
**Params:** string $mime_type
**Since:** 3.5 | **Tags:** #Modern
Filters default mime type prior to getting the file extension.

### image_editor_save_pre
**Params:** WP_Image_Editor $image, int $attachment_id
**Since:** 3.5 | **Tags:** #Modern
Filters the WP_Image_Editor instance for the image to be streamed to the browser.

### manage_taxonomies_for_attachment_columns
**Params:** string[] $taxonomies, string $post_type
**Since:** 3.5 | **Tags:** #Modern
Filters the taxonomy columns for attachments in the Media list table.

### media_view_settings
**Params:** array $settings, WP_Post $post
**Since:** 3.5 | **Tags:** #Modern
Filters the media view settings.

### media_view_strings
**Params:** string[] $strings, WP_Post $post
**Since:** 3.5 | **Tags:** #Modern
Filters the media view strings.

### mime_types
**Params:** string[] $wp_get_mime_types
**Since:** 3.5 | **Tags:** #Modern
Filters the list of mime types and file extensions. This filter should be used to add, not remove, mime types. To remove mime types, use the {@see 'upload_mimes'} filter.

### wp_editor_set_quality
**Params:** int $quality, string $mime_type, array $size
**Since:** 3.5 | **Tags:** #Modern
Filters the default image compression quality setting. Applies only during initial editor instantiation, or when set_quality() is run manually without the `$quality` argument. The WP_Image_Editor::set_quality() method has priority over the filter.

### wp_image_editors
**Params:** string[] $image_editors
**Since:** 3.5 | **Tags:** #Modern
Filters the list of image editing library classes.

### wp_image_editor_before_change
**Params:** WP_Image_Editor $image, array $changes
**Since:** 3.5 | **Tags:** #Modern
Filters the WP_Image_Editor instance before applying changes to the image.

### wp_prepare_attachment_for_js
**Params:** array $response, WP_Post $attachment, array|false $meta
**Since:** 3.5 | **Tags:** #Modern
Filters the attachment data prepared for JavaScript.

### wp_save_image_editor_file
**Params:** bool|null $override, string $filename, WP_Image_Editor $image, string $mime_type, int $post_id
**Since:** 3.5 | **Tags:** #Modern
Filters whether to skip saving the image file. Returning a non-null value will short-circuit the save method, returning that value instead.

### get_attached_media
**Params:** WP_Post[] $children, string $type, WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters the list of media attached to the given post.

### get_attached_media_args
**Params:** array $args, string $type, WP_Post $post
**Since:** 3.6 | **Tags:** #Modern
Filters arguments used to retrieve media attached to the given post.

### wp_audio_embed_handler
**Since:** 3.6 | **Tags:** #Modern

### wp_audio_extensions
**Params:** string[] $extensions
**Since:** 3.6 | **Tags:** #Modern
Filters the list of supported audio formats.

### wp_audio_shortcode
**Params:** string $html, array $atts, string $audio, int $post_id, string $library
**Since:** 3.6 | **Tags:** #Modern
Filters the audio shortcode output.

### wp_audio_shortcode_class
**Since:** 3.6 | **Tags:** #Modern

### wp_audio_shortcode_library
**Params:** string $library
**Since:** 3.6 | **Tags:** #Modern
Filters the media library used for the audio shortcode.

### wp_video_embed_handler
**Since:** 3.6 | **Tags:** #Modern

### wp_video_extensions
**Params:** string[] $extensions
**Since:** 3.6 | **Tags:** #Modern
Filters the list of supported video formats.

### wp_video_shortcode
**Params:** string $output, array $atts, string $video, int $post_id, string $library
**Since:** 3.6 | **Tags:** #Modern
Filters the output of the video shortcode.

### wp_video_shortcode_class
**Since:** 3.6 | **Tags:** #Modern

### wp_video_shortcode_library
**Params:** string $library
**Since:** 3.6 | **Tags:** #Modern
Filters the media library used for the video shortcode.

### img_caption_shortcode_width
**Params:** int $width, array $atts, string $content
**Since:** 3.7 | **Tags:** #Modern
Filters the width of an image's caption. By default, the caption is 10 pixels greater than the width of the image, to prevent post content from running up against a floated image.

### media_submitbox_misc_sections
**Params:** array $fields, WP_Post $post
**Since:** 3.7 | **Tags:** #Modern
Filters the audio and video metadata fields to be shown in the publish meta box. The key for each item in the array should correspond to an attachment metadata key, and the value should be the desired label.

### wp_audio_shortcode_override
**Params:** string $html, array $attr, string $content, int $instance
**Since:** 3.7 | **Tags:** #Modern
Filters the default audio shortcode output. If the filtered output isn't empty, it will be used instead of generating the default audio template.

### wp_video_shortcode_override
**Params:** string $html, array $attr, string $content, int $instance
**Since:** 3.7 | **Tags:** #Modern
Filters the default video shortcode output. If the filtered output isn't empty, it will be used instead of generating the default video template.

### attachment_thumbnail_args
**Params:** array $image_attachment, array $metadata, array $uploaded
**Since:** 3.9 | **Tags:** #Modern
Filters the parameters for the attachment thumbnail creation.

### wp_get_attachment_id3_keys
**Params:** array $fields, WP_Post $attachment, string $context
**Since:** 3.9 | **Tags:** #Modern
Filters the editable list of keys to look up data from an attachment's metadata.

### wp_editor_expand
**Params:** bool $expand, string $post_type
**Since:** 4.0 | **Tags:** #Modern
Filters whether to enable the 'expand' functionality in the post editor.

### wp_editor_settings
**Params:** array $settings, string $editor_id
**Since:** 4.0 | **Tags:** #Modern
Filters the wp_editor() settings.

### image_add_caption_text
**Params:** string $caption, int $id
**Since:** 4.1 | **Tags:** #Modern
Filters the caption text. Note: If the caption text is empty, the caption shortcode will not be appended to the image HTML when inserted into the editor. Passing an empty value also prevents the {@see 'image_add_caption_shortcode'} Filters from being evaluated at the end of image_add_caption().

### attachment_url_to_postid
**Params:** int|null $post_id, string $url
**Since:** 4.2 | **Tags:** #Modern
Filters an attachment ID found by URL.

### emoji_ext
**Since:** 4.2 | **Tags:** #Modern

### emoji_url
**Since:** 4.2 | **Tags:** #Modern

### get_avatar_data
**Params:** array $args, mixed $id_or_email
**Since:** 4.2 | **Tags:** #Modern
Filters the avatar data.

### get_avatar_url
**Since:** 4.2 | **Tags:** #Modern

### media_embedded_in_content_allowed_types
**Params:** string[] $allowed_media_types
**Since:** 4.2 | **Tags:** #Modern
Filters the embedded media types that are allowed to be returned from the content blob.

### pre_get_avatar
**Params:** string|null $avatar, mixed $id_or_email, array $args
**Since:** 4.2 | **Tags:** #Modern
Allows the HTML for a user's avatar to be returned early. Returning a non-null value will effectively short-circuit get_avatar(), passing the value through the {@see 'get_avatar'} filter and returning early.

### pre_get_avatar_data
**Params:** array $args, mixed $id_or_email
**Since:** 4.2 | **Tags:** #Modern
Filters whether to retrieve the avatar URL early. Passing a non-null value in the 'url' member of the return array will effectively short circuit get_avatar_data(), passing the value through the {@see 'get_avatar_data'} filter and returning early.

### editor_stylesheets
**Params:** string[] $stylesheets
**Since:** 4.3 | **Tags:** #Modern
Filters the array of URLs of stylesheets applied to the editor.

### site_icon_attachment_metadata
**Params:** array $metadata
**Since:** 4.3 | **Tags:** #Modern
Filters the site icon attachment metadata.

### site_icon_image_sizes
**Params:** int[] $site_icon_sizes
**Since:** 4.3 | **Tags:** #Modern
Filters the different dimensions that a site icon is saved in.

### site_icon_meta_tags
**Params:** string[] $meta_tags
**Since:** 4.3 | **Tags:** #Modern
Filters the site icon meta tags, so plugins can add their own.

### wp_get_attachment_image_src
**Params:** array|false $image, int $attachment_id, string|int[] $size, bool $icon
**Since:** 4.3 | **Tags:** #Modern
Filters the attachment image source result.

### get_header_image_tag
**Params:** string $html, object $header, array $attr
**Since:** 4.4 | **Tags:** #Modern
Filters the markup of header images.

### image_get_intermediate_size
**Params:** array $data, int $post_id, string|int[] $size
**Since:** 4.4 | **Tags:** #Modern
Filters the output of image_get_intermediate_size()

### max_srcset_image_width
**Params:** int $max_width, int[] $size_array
**Since:** 4.4 | **Tags:** #Modern
Filters the maximum image width to be included in a 'srcset' attribute.

### mejs_settings
**Params:** array $mejs_settings
**Since:** 4.4 | **Tags:** #Modern
Filters the MediaElement configuration settings.

### image_strip_meta
**Params:** bool $strip_meta
**Since:** 4.5 | **Tags:** #Modern
Filters whether to strip metadata from images when they're resized. This filter only applies when resizing using the Imagick editor since GD always strips profiles by default.

### emoji_svg_ext
**Since:** 4.6 | **Tags:** #Modern

### emoji_svg_url
**Since:** 4.6 | **Tags:** #Modern

### wp_get_attachment_caption
**Params:** string $caption, int $post_id
**Since:** 4.6 | **Tags:** #Modern
Filters the attachment caption.

### fallback_intermediate_image_sizes
**Params:** string[] $fallback_sizes, array $metadata
**Since:** 4.7 | **Tags:** #Modern
Filters the image sizes generated for non-image mime types.

### header_video_settings
**Params:** array $settings
**Since:** 4.7 | **Tags:** #Modern
Filters header video settings.

### is_header_video_active
**Params:** bool $show_video
**Since:** 4.7 | **Tags:** #Modern
Filters whether the custom header video is eligible to show on the current page.

### smilies
**Params:** string[] $wpsmiliestrans
**Since:** 4.7 | **Tags:** #Modern
Filters all the smilies. This filter must be added before `smilies_init` is run, as it is normally only run once to setup the smilies regex.

### get_header_video_url
**Params:** string $url
**Since:** 4.8 | **Tags:** #Modern
Filters the header video URL.

### media_library_months_with_files
**Params:** stdClass[]|null $months
**Since:** 4.8 | **Tags:** #Modern
Allows overriding the list of months displayed in the media library. By default (if this filter does not return an array), a query will be run to determine the months that have media items.  This query can be expensive for large media libraries, so it may be desirable for sites to override this behavior.

### media_library_show_audio_playlist
**Params:** bool|null $show
**Since:** 4.8 | **Tags:** #Modern
Allows showing or hiding the "Create Audio Playlist" button in the media library. By default, the "Create Audio Playlist" button will always be shown in the media library.  If this filter returns `null`, a query will be run to determine whether the media library contains any audio items.  This was the default behavior prior to version 4.8.0, but this query is expensive for large media libraries.

### media_library_show_video_playlist
**Params:** bool|null $show
**Since:** 4.8 | **Tags:** #Modern
Allows showing or hiding the "Create Video Playlist" button in the media library. By default, the "Create Video Playlist" button will always be shown in the media library.  If this filter returns `null`, a query will be run to determine whether the media library contains any video items.  This was the default behavior prior to version 4.8.0, but this query is expensive for large media libraries.

### pre_move_uploaded_file
**Params:** mixed $move_new_file, array $file, string $new_file, string $type
**Since:** 4.9 | **Tags:** #Modern
Filters whether to short-circuit moving the uploaded file after passing all checks. If a non-null value is returned from the filter, moving the file and any related error reporting will be completely skipped.

### big_image_size_threshold
**Params:** int $threshold, array $imagesize, string $file, int $attachment_id
**Since:** 5.3 | **Tags:** #Recent
Filters the "BIG image" threshold value. If the original image width or height is above the threshold, it will be scaled down. The threshold is used as max width and max height. The scaled down image will be used as the largest available size, including the `_wp_attached_file` post meta value. Returning `false` from the filter callback will disable the scaling.

### wp_get_missing_image_subsizes
**Params:** array[] $missing_sizes, array $image_meta, int $attachment_id
**Since:** 5.3 | **Tags:** #Recent
Filters the array of missing image sub-sizes for an uploaded image.

### wp_image_maybe_exif_rotate
**Params:** int $orientation, string $file
**Since:** 5.3 | **Tags:** #Recent
Filters the `$orientation` value to correct it before rotating or to prevent rotating the image.

### wp_image_resize_identical_dimensions
**Params:** bool $proceed, int $orig_w, int $orig_h
**Since:** 5.3 | **Tags:** #Recent
Filters whether to proceed with making an image sub-size with identical dimensions with the original/source image. Differences of 1px may be due to rounding and are ignored.

### pre_delete_attachment
**Params:** WP_Post|false|null $delete, WP_Post $post, bool $force_delete
**Since:** 5.5 | **Tags:** #Recent
Filters whether an attachment deletion should take place.

### pre_wp_unique_filename_file_list
**Params:** array|null $files, string $dir, string $filename
**Since:** 5.5 | **Tags:** #Recent
Filters the file list used for calculating a unique filename for a newly added file. Returning an array from the filter will effectively short-circuit retrieval from the filesystem and return the passed value instead.

### safecss_filter_attr_allow_css
**Params:** bool $allow_css, string $css_test_string
**Since:** 5.5 | **Tags:** #Recent
Filters the check for unsafe CSS in `safecss_filter_attr`. Enables developers to determine whether a section of CSS should be allowed or discarded. By default, the value will be false if the part contains \ ( & } = or comments. Return true to allow the CSS part to be included in the output.

### wp_image_file_matches_image_meta
**Params:** bool $match, string $image_location, array $image_meta, int $attachment_id
**Since:** 5.5 | **Tags:** #Recent
Filters whether an image path or URI matches image meta.

### image_sideload_extensions
**Params:** string[] $allowed_extensions, string $file
**Since:** 5.6 | **Tags:** #Recent
Filters the list of allowed file extensions when sideloading an image from a URL. The default allowed extensions are: - `jpg` - `jpeg` - `jpe` - `png` - `gif` - `webp`

### wp_get_attachment_image
**Params:** string $html, int $attachment_id, string|int[] $size, bool $icon, string[] $attr
**Since:** 5.6 | **Tags:** #Recent
Filters the HTML img element representing an image attachment.

### wp_image_src_get_dimensions
**Params:** array|false $dimensions, string $image_src, array $image_meta, int $attachment_id
**Since:** 5.7 | **Tags:** #Recent
Filters the wp_image_src_get_dimensions() value.

### image_editor_output_format
**Params:** string[] $output_format, string $filename, string $mime_type
**Since:** 5.8 | **Tags:** #Recent
Filters the image editor output format mapping. Enables filtering the mime type used to save images. By default HEIC/HEIF images are converted to JPEGs.

### media_library_infinite_scrolling
**Params:** bool $infinite
**Since:** 5.8 | **Tags:** #Recent
Filters whether the Media Library grid has infinite scrolling. Default `false`.

### get_header_image_tag_attributes
**Params:** array $attr, object $header
**Since:** 5.9 | **Tags:** #Recent
Filters the list of header image attributes.

### post_thumbnail_id
**Params:** int|false $thumbnail_id, int|WP_Post|null $post
**Since:** 5.9 | **Tags:** #Recent
Filters the post thumbnail ID.

### post_thumbnail_url
**Params:** string|false $thumbnail_url, int|WP_Post|null $post, string|int[] $size
**Since:** 5.9 | **Tags:** #Recent
Filters the post thumbnail URL.

### media_date_column_time
**Params:** string $h_time, WP_Post $post, string $column_name
**Since:** 6.0 | **Tags:** #Recent
Filters the published time of an attachment displayed in the Media list table.

### pre_wp_filesize
**Params:** null|int $size, string $path
**Since:** 6.0 | **Tags:** #Recent
Filters the result of wp_filesize() before the file_exists() PHP function is run.

### get_header_image
**Params:** string $url
**Since:** 6.1 | **Tags:** #Recent
Filters the header image URL.

### wp_get_attachment_link_attributes
**Params:** array $attributes, int $id
**Since:** 6.2 | **Tags:** #Recent
Filters the list of attachment link attributes.

### image_edit_thumbnails_separately
**Params:** bool $show
**Since:** 6.3 | **Tags:** #Recent
Shows the settings in the Image Editor that allow selecting to edit only the thumbnail of an image.

### wp_get_attachment_image_context
**Params:** string $context
**Since:** 6.3 | **Tags:** #Recent
Filters the context in which wp_get_attachment_image() is used.

### pre_unzip_file
**Params:** null|true|WP_Error $result, string $file, string $to, string[] $needed_dirs, float $required_space
**Since:** 6.4 | **Tags:** #Recent
Filters archive unzipping to override with a custom process.

### unzip_file
**Params:** true|WP_Error $result, string $file, string $to, string[] $needed_dirs, float $required_space
**Since:** 6.4 | **Tags:** #Recent
Filters the result of unzipping an archive.

### font_dir
**Params:** array $font_dir
**Since:** 6.5 | **Tags:** #Recent
Filters the fonts directory data. This filter allows developers to modify the fonts directory data.

### image_save_progressive
**Params:** bool $interlace, string $mime_type
**Since:** 6.5 | **Tags:** #Recent
Filters whether to output progressive images (if available).

### pre_attachment_url_to_postid
**Params:** int|null $post_id, string $url
**Since:** 6.7 | **Tags:** #Recent
Filters the attachment ID to allow short-circuit the function. Allows plugins to short-circuit attachment ID lookups. Plugins making use of this function should return: - 0 (integer) to indicate the attachment is not found, - attachment ID (integer) to indicate the attachment ID found, - null to indicate WordPress should proceed with the lookup. Warning: The post ID may be null or zero, both of which cast to a boolean false. For information about casting to booleans see the {@link https://www.php.net/manual/en/language.types.boolean.php PHP documentation}. Use the === operator for testing the post ID when developing filters using this hook.

### image_max_bit_depth
**Params:** int $max_depth, int $image_depth
**Since:** 6.8 | **Tags:** #Recent
Filters the maximum bit depth of resized images. This filter only applies when resizing using the Imagick editor since GD does not support getting or setting bit depth. Use this to adjust the maximum bit depth of resized images.

## Sources

- [WordPress Hook Reference (adambrown.info)](https://adambrown.info/p/wp_hooks)
- [developer.wordpress.org — Plugin API](https://developer.wordpress.org/plugins/hooks/)
- Extracted from local WordPress core docblocks (`apply_filters` / `do_action` calls)
