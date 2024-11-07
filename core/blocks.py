from wagtail.blocks import StructBlock, PageChooserBlock


class FeaturedPageBlock(StructBlock):
    featured_page = PageChooserBlock()
    class Meta:
        template = 'core/blocks/featured_page.html'
