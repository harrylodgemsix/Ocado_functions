FIELDS_FOR_CAMPAIGNS = """
    campaign_id,
    impressions
    """

FIELDS_FOR_ADS = """
    account_name,
    account_id,
    ad_name,
    ad_id,
    adset_name,
    adset_id,
    campaign_name,
    campaign_id,
    account_currency,
    action_values,
    actions,
    attribution_setting,
    buying_type,
    canvas_avg_view_time,
    catalog_segment_value,
    clicks,
    conversion_rate_ranking,
    conversion_values,
    conversions,
    converted_product_quantity,
    converted_product_value,
    cost_per_action_type,
    cost_per_conversion,
    cost_per_estimated_ad_recallers,
    cost_per_inline_link_click,
    cost_per_inline_post_engagement,
    cost_per_outbound_click,
    cost_per_thruplay,
    cost_per_unique_action_type,
    cost_per_unique_click,
    cost_per_unique_inline_link_click,
    cost_per_unique_outbound_click,
    cpc,
    cpm,
    cpp,
    ctr,
    engagement_rate_ranking,
    estimated_ad_recall_rate,
    estimated_ad_recallers,
    frequency,
    full_view_impressions,
    full_view_reach,
    impressions,
    inline_link_click_ctr,
    inline_link_clicks,
    inline_post_engagement,
    instant_experience_clicks_to_open,
    instant_experience_clicks_to_start,
    instant_experience_outbound_clicks,
    mobile_app_purchase_roas,
    objective,
    outbound_clicks,
    outbound_clicks_ctr,
    place_page_name,
    purchase_roas,
    qualifying_question_qualify_answer_rate,
    quality_ranking,
    reach,
    social_spend,
    spend,
    unique_actions,
    unique_clicks,
    unique_ctr,
    unique_inline_link_click_ctr,
    unique_inline_link_clicks,
    unique_link_clicks_ctr,
    unique_outbound_clicks,
    unique_outbound_clicks_ctr,
    video_30_sec_watched_actions,
    video_avg_time_watched_actions,
    video_p100_watched_actions,
    video_p25_watched_actions,
    video_p50_watched_actions,
    video_p75_watched_actions,
    video_p95_watched_actions,
    video_play_actions,
    video_play_curve_actions,
    website_ctr,
    website_purchase_roas
    """


FIELDS = [
    "account_name",
    "account_id",
    "ad_name",
    "ad_id",
    "adset_name",
    "adset_id",
    "campaign_name",
    "campaign_id",
    "publisher_platform",
    "platform_position",
    "impression_device",
    "date_start",
    "date_stop",
    "account_currency",
    "action_values",
    "actions",
    "attribution_setting",
    "buying_type",
    "canvas_avg_view_time",
    "catalog_segment_value",
    "clicks",
    "conversion_rate_ranking",
    "conversion_values",
    "conversions",
    "converted_product_quantity",
    "converted_product_value",
    "cost_per_action_type",
    "cost_per_conversion",
    "cost_per_estimated_ad_recallers",
    "cost_per_inline_link_click",
    "cost_per_inline_post_engagement",
    "cost_per_outbound_click",
    "cost_per_thruplay",
    "cost_per_unique_action_type",
    "cost_per_unique_click",
    "cost_per_unique_inline_link_click",
    "cost_per_unique_outbound_click",
    "cpc",
    "cpm",
    "cpp",
    "ctr",
    "engagement_rate_ranking",
    "estimated_ad_recall_rate",
    "estimated_ad_recallers",
    "frequency",
    "full_view_impressions",
    "full_view_reach",
    "impressions",
    "inline_link_click_ctr",
    "inline_link_clicks",
    "inline_post_engagement",
    "instant_experience_clicks_to_open",
    "instant_experience_clicks_to_start",
    "instant_experience_outbound_clicks",
    "mobile_app_purchase_roas",
    "objective",
    "outbound_clicks",
    "outbound_clicks_ctr",
    "place_page_name",
    "purchase_roas",
    "qualifying_question_qualify_answer_rate",
    "quality_ranking",
    "reach",
    "social_spend",
    "spend",
    "unique_actions",
    "unique_clicks",
    "unique_ctr",
    "unique_inline_link_click_ctr",
    "unique_inline_link_clicks",
    "unique_link_clicks_ctr",
    "unique_outbound_clicks",
    "unique_outbound_clicks_ctr",
    "video_30_sec_watched_actions",
    "video_avg_time_watched_actions",
    "video_p100_watched_actions",
    "video_p25_watched_actions",
    "video_p50_watched_actions",
    "video_p75_watched_actions",
    "video_p95_watched_actions",
    "video_play_actions",
    "video_play_curve_actions",
    "website_ctr",
    "website_purchase_roas"]

ACTION_TYPE_LIST = [
    "app_custom_event.fb_mobile_achievement_unlocked",
    "app_custom_event.fb_mobile_activate_app",
    "app_custom_event.fb_mobile_add_payment_info",
    "app_custom_event.fb_mobile_add_to_cart",
    "app_custom_event.fb_mobile_add_to_wishlist",
    "app_custom_event.fb_mobile_complete_registration",
    "app_custom_event.fb_mobile_content_view",
    "app_custom_event.fb_mobile_initiated_checkout",
    "app_custom_event.fb_mobile_level_achieved",
    "app_custom_event.fb_mobile_purchase",
    "app_custom_event.fb_mobile_rate",
    "app_custom_event.fb_mobile_search",
    "app_custom_event.fb_mobile_spent_credits",
    "app_custom_event.fb_mobile_tutorial_completion",
    "app_custom_event.other",
    "app_install",
    "app_use",
    "checkin",
    "comment",
    "credit_spent",
    "games.plays",
    "landing_page_view",
    "like",
    "link_click",
    "mobile_app_install",
    "offsite_conversion.fb_pixel_add_payment_info",
    "offsite_conversion.fb_pixel_add_to_cart",
    "offsite_conversion.fb_pixel_add_to_wishlist",
    "offsite_conversion.fb_pixel_complete_registration",
    "offsite_conversion.fb_pixel_custom",
    "offsite_conversion.fb_pixel_initiate_checkout",
    "offsite_conversion.fb_pixel_lead",
    "offsite_conversion.fb_pixel_purchase",
    "offsite_conversion.fb_pixel_search",
    "offsite_conversion.fb_pixel_view_content",
    "onsite_conversion.flow_complete",
    "onsite_conversion.messaging_block",
    "onsite_conversion.messaging_conversation_started_7d",
    "onsite_conversion.messaging_first_reply",
    "onsite_conversion.post_save",
    "onsite_conversion.purchase",
    "photo_view",
    "post",
    "post_reaction",
    "rsvp",
    "video_view",
    "contact_total",
    "contact_website",
    "contact_mobile_app",
    "contact_offline",
    "customize_product_total",
    "customize_product_website",
    "customize_product_mobile_app",
    "customize_product_offline",
    "donate_total",
    "donate_website",
    "donate_on_facebook",
    "donate_mobile_app",
    "donate_offline",
    "find_location_total",
    "find_location_website",
    "find_location_mobile_app",
    "find_location_offline",
    "schedule_total",
    "schedule_website",
    "schedule_mobile_app",
    "schedule_offline",
    "start_trial_total",
    "start_trial_website",
    "start_trial_mobile_app",
    "start_trial_offline",
    "submit_application_total",
    "submit_application_website",
    "submit_application_mobile_app",
    "submit_application_offline",
    "submit_application_on_facebook",
    "subscribe_total",
    "subscribe_website",
    "subscribe_mobile_app",
    "subscribe_offline",
    "recurring_subscription_payment_total",
    "recurring_subscription_payment_website",
    "recurring_subscription_payment_mobile_app",
    "recurring_subscription_payment_offline",
    "cancel_subscription_total",
    "cancel_subscription_website",
    "cancel_subscription_mobile_app",
    "cancel_subscription_offline",
    "ad_click_mobile_app",
    "ad_impression_mobile_app",
    "click_to_call_call_confirm",
    "page_engagement",
    "post_engagement",
    "onsite_conversion.lead_grouped",
    "lead",
    "leadgen_grouped",
    "omni_app_install",
    "omni_purchase",
    "omni_add_to_cart",
    "omni_complete_registration",
    "omni_view_content",
    "omni_search",
    "omni_initiated_checkout",
    "omni_achievement_unlocked",
    "omni_activate_app",
    "omni_level_achieved",
    "omni_rate",
    "omni_spend_credits",
    "omni_tutorial_completion"]

NEW_COL_NAME = [
    "mobile_app_feature_unlocks",
    "mobile_app_starts",
    "mobile_app_payment_details",
    "mobile_app_adds_to_cart",
    "mobile_app_adds_to_wishlist",
    "mobile_app_registrations",
    "mobile_app_content_views",
    "mobile_app_checkouts",
    "mobile_app_achievements",
    "mobile_app_purchases",
    "mobile_app_ratings",
    "mobile_app_searchs",
    "mobile_app_credit_spends",
    "mobile_app_tutorial_completions",
    "other_mobile_app_actions",
    "app_installs",
    "app_uses",
    "check_ins",
    "post_comments",
    "credit_spends",
    "game_plays",
    "landing_page_views",
    "page_likes",
    "link_clicks",
    "mobile_app_installs",
    "adds_payment_info",
    "adds_to_cart",
    "adds_to_wishlist",
    "completed_registration",
    "custom_pixel_events_defined_by_the_advertiser",
    "initiates_checkout",
    "leads",
    "purchases",
    "searchs",
    "views_content",
    "on_facebook_workflow_completions",
    "blocked_messaging_conversations",
    "messaging_conversations_started",
    "new_messaging_conversations",
    "post_saves",
    "on_facebook_purchases",
    "page_photo_views",
    "post_shares",
    "post_reactions",
    "event_responses",
    "video_views_3_seconds",
    "contacts",
    "website_contacts",
    "mobile_app_contacts",
    "offline_contacts",
    "products_customized",
    "website_products_customized",
    "mobile_app_products_customized",
    "offline_products_customized",
    "donations",
    "website_donations",
    "on_facebook_donations",
    "mobile_app_donations",
    "offline_donations",
    "location_searches",
    "website_location_searches",
    "mobile_app_location_searches",
    "offline_app_location_searches",
    "appointments_scheduled",
    "website_appointments_scheduled",
    "mobile_app_appointments_scheduled",
    "offline_app_appointments_scheduled",
    "trials_started",
    "website_trials_started",
    "mobile_app_trials_started",
    "offline_trials_started",
    "applications_submitted",
    "website_applications_submitted",
    "mobile_app_applications_submitted",
    "offline_applications_submitted",
    "on_facebook_applications_submitted",
    "subscriptions",
    "website_subscriptions",
    "mobile_app_subscriptions",
    "offline_subscriptions",
    "recurring_subscription_payments",
    "website_recurring_subscription_payments",
    "mobile_app_recurring_subscription_payments",
    "offline_recurring_subscription_payments",
    "canceled_subscriptions",
    "website_canceled_subscriptions",
    "mobile_app_canceled_subscriptions",
    "offline_canceled_subscriptions",
    "in_app_ad_clicks",
    "in_app_ad_impressions",
    "call_confirmation_clicks",
    "page_engagement",
    "post_engagement",
    "all_on_facebook_leads",
    "all_offsite_leads_plus_all_on_facebook_leads",
    "on_facebook_leads_coming_from_messenger_and_instant_forms",
    "omni_app_installs",
    "omni_purchases",
    "omni_adds_to_cart",
    "omni_registrations_completed",
    "omni_content_views",
    "omni_searches",
    "omni_checkouts_initiated",
    "omni_achievements_unlocked",
    "omni_app_activations",
    "omni_levels_achieved",
    "omni_ratings_submitted",
    "omni_credit_spends",
    "omni_tutorials_completed"]
