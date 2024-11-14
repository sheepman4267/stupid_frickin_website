from wagtail.blocks import StructBlock, PageChooserBlock, StaticBlock


class FeaturedPageBlock(StructBlock):
    featured_page = PageChooserBlock()

    class Meta:
        template = 'core/blocks/featured_page.html'


class RecentPostsBlock(StaticBlock):
    class Meta:
        template = 'core/blocks/recent_posts.html'
        admin_text = 'Show a list of recent posts from this page'
