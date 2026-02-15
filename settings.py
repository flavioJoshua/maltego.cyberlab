from maltego_trx.decorator_registry import TransformSetting

api_key_setting = TransformSetting(name='ICT_api_key',
                                   display_name='API Key',
                                   setting_type='string',
                                   global_setting=True)

language_setting = TransformSetting(name='language',
                                    display_name="Language",
                                    setting_type='string',
                                    default_value='en',
                                    optional=True,
                                    popup=True)


valori_setting = TransformSetting(name='valori',
                                    display_name="Valori  visibili",
                                    setting_type='string',
                                    default_value='qualcosa',
                                    optional=True,
                                    popup=True)

# Brave Search transform inputs (string-only, optional)
brave_count_setting = TransformSetting(
    name="count",
    display_name="count",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_offset_setting = TransformSetting(
    name="offset",
    display_name="offset",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_freshness_setting = TransformSetting(
    name="freshness",
    display_name="freshness",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_country_setting = TransformSetting(
    name="country",
    display_name="country",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_search_lang_setting = TransformSetting(
    name="search_lang",
    display_name="search_lang",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_extra_snippets_setting = TransformSetting(
    name="extra_snippets",
    display_name="extra_snippets",
    setting_type="string",
    optional=True,
    popup=True,
)
brave_goggles_setting = TransformSetting(
    name="goggles",
    display_name="goggles",
    setting_type="string",
    optional=True,
    popup=True,
)

brave_web_news_transform_settings = [
    brave_count_setting,
    brave_offset_setting,
    brave_freshness_setting,
    brave_country_setting,
    brave_search_lang_setting,
    brave_extra_snippets_setting,
    brave_goggles_setting,
]

brave_image_transform_settings = [
    brave_count_setting,
    brave_country_setting,
    brave_search_lang_setting,
]
