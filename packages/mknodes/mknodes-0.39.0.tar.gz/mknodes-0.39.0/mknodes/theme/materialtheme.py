from __future__ import annotations

from collections.abc import MutableMapping
import functools
import pathlib

from typing import Literal

from mknodes.basenodes import mknode
from mknodes.cssclasses import cssclasses, rootcss
from mknodes.data import datatypes
from mknodes.theme import mkblog, theme
from mknodes.theme.material import palette
from mknodes.utils import helpers, log, reprhelpers


logger = log.get_logger(__name__)


COLORS = {
    "red": {"color": "#ef5552", "text": "#ffffff"},
    "pink": {"color": "#e92063", "text": "#ffffff"},
    "purple": {"color": "#ab47bd", "text": "#ffffff"},
    "deep purple": {"color": "#7e56c2", "text": "#ffffff"},
    "indigo": {"color": "#4051b5", "text": "#ffffff"},
    "blue": {"color": "#2094f3", "text": "#ffffff"},
    "light blue": {"color": "#02a6f2", "text": "#ffffff"},
    "cyan": {"color": "#00bdd6", "text": "#ffffff"},
    "teal": {"color": "#009485", "text": "#ffffff"},
    "green": {"color": "#4cae4f", "text": "#ffffff"},
    "light green": {"color": "#8bc34b", "text": "#ffffff"},
    "lime": {"color": "#cbdc38", "text": "#000000"},
    "yellow": {"color": "#ffec3d", "text": "#000000"},
    "amber": {"color": "#ffc105", "text": "#000000"},
    "orange": {"color": "#ffa724", "text": "#000000"},
    "deep orange": {"color": "#ff6e42", "text": "#ffffff"},
    "brown": {"color": "#795649", "text": "#ffffff"},
    "grey": {"color": "#757575", "text": "#ffffff"},
    "blue grey": {"color": "#546d78", "text": "#ffffff"},
    "black": {"color": "#000000", "text": "#ffffff"},
    "white": {"color": "#ffffff", "text": "#000000"},
    "custom": {"color": "#000000", "text": "#FFFFFF"},
}


IconTypeStr = Literal[
    "footnotes",
    "details",
    "previous_tab",
    "next_tab",
    "tasklist",
    "tasklist_checked",
]

ICON_TYPE: dict[IconTypeStr, str] = dict(
    footnotes="md-footnotes-icon",
    details="md-details-icon",
    previous_tab="md-tabbed-icon--prev",
    next_tab="md-tabbed-icon--next",
    tasklist="md-tasklist-icon",
    tasklist_checked="md-tasklist-icon--checked",
)


def build_badge(icon: str, text: str = "", typ: str = ""):
    classes = f"mdx-badge mdx-badge--{typ}" if typ else "mdx-badge"
    lines = [f'<span class="{classes}">']
    if icon:
        lines.append(f'<span class="mdx-badge__icon">{icon}</span>')
    if text:
        lines.append(f'<span class="mdx-badge__icon">{text}</span>')
    lines.append("</span>")
    return "".join(lines)


CONTAINER_RULE = """.mdx-container {
  padding-top: px2rem(20px);
  background:
    url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1123 258'><path d='M1124,2c0,0 0,256 0,256l-1125,0l0,-48c0,0 16,5 55,5c116,0 197,-92 325,-92c121,0 114,46 254,46c140,0 214,-167 572,-166Z' style='fill: hsla(0, 0%, 100%, 1)' /></svg>") no-repeat bottom,
    linear-gradient(
      to bottom,
      var(--md-primary-fg-color),
      hsla(280, 67%, 55%, 1) 99%,
      var(--md-default-bg-color) 99%
    );
    }
"""  # noqa: E501


def get_partial_path(partial: str) -> pathlib.Path:
    import material

    path = pathlib.Path(material.__path__[0])
    return path / "partials" / f"{partial}.html"


class MdxContainerRule(cssclasses.StyleRule):
    def __init__(self):
        super().__init__(CONTAINER_RULE)


class MaterialTheme(theme.Theme):
    """Material Theme."""

    name = "material"

    def __init__(self, **kwargs):
        super().__init__(self.name, **kwargs)
        self.css = rootcss.RootCSS()
        self.main_template = self.templates["main.html"]
        self._foreground_color = None
        self.blog = mkblog.MkBlog()
        self.features = self.data.get("features")

    def __repr__(self):
        return reprhelpers.get_repr(self)

    @functools.cached_property
    def palettes(self) -> list[palette.Palette]:
        data = self.data.get("palette")
        if not data:
            return [palette.Palette()]
        if isinstance(data, dict):
            data = [data]
        return [
            palette.Palette(
                primary=pal.get("primary", "indigo"),
                accent=pal.get("accent", "indigo"),
                scheme=pal.get("scheme", "default"),
                media=pal.get("media"),
                toggle_name=pal.get("toggle", {}).get("name"),
                toggle_icon=pal.get("toggle", {}).get("icon"),
            )
            for pal in data
        ]

    def iter_nodes(self):
        if isinstance(self.announcement_bar, mknode.MkNode):
            yield 0, self.announcement_bar

    @property
    def announcement_bar(self):
        return self.main_template.announcement_bar

    @announcement_bar.setter
    def announcement_bar(self, value):
        if isinstance(value, mknode.MkNode):
            value.associated_project = self.associated_project
        self.main_template.announcement_bar = value

    def get_accent_color(self) -> str:
        # sourcery skip: use-or-for-fallback
        color = self._get_color("accent", fallback="")
        if not color:
            color = self._get_color("primary", fallback="indigo")
        return COLORS[color]["color"]

    def _get_color(self, color_type: Literal["primary", "accent"], fallback: str) -> str:
        pal = self.palettes[0]
        match color_type:
            case "primary":
                return pal.primary or fallback
            case "accent":
                return pal.accent or fallback

    def set_color(self, color_type: Literal["primary", "accent"], value: str):
        pal = self.palettes[0]
        match color_type:
            case "primary":
                pal.primary = value
            case "accent":
                pal.accent = value

    def set_accent_foreground_color(self, color: datatypes.RGBColorType):
        color_str = helpers.get_color_str(color)
        self.css[":root"]["--md-accent-fg-color"] = color_str
        self.css[":root"]["--md-accent-fg-color--transparent"] = color_str
        self.set_color("accent", "custom")
        return color_str

    def set_primary_background_color(
        self,
        color: datatypes.RGBColorType,
    ):
        self.set_color("primary", "custom")
        color_str = helpers.get_color_str(color)
        self.css[":root"]["--md-primary-bg-color"] = color_str
        self.css[":root"]["--md-primary-bg-color--light"] = color_str
        return color_str

    @property
    def primary_color(self) -> str:
        if self._foreground_color:
            return self._foreground_color
        color = self._get_color("primary", fallback="indigo")
        return COLORS[color]["color"]

    @property
    def _text_color(self):
        color = self._get_color("primary", fallback="indigo")
        return COLORS[color]["text"]

    def set_content_area_width(self, width: int):
        self.css.add_rule(".md-grid", {"max-width": f"{width}px"})

    def set_tooltip_width(self, height: int):
        self.css[":root"]["--md-tooltip-width"] = f"{height}px"

    def set_classic_admonition_style(self):
        self.css.add_rule(
            ".md-typeset .admonition, .md-typeset details",
            {"border-width": 0, "border-left-width": "4px"},
        )

    def add_admonition_type(
        self,
        name: str,
        data: str,
        header_color: datatypes.ColorType,
        icon_color: datatypes.ColorType | None = None,
        border_color: datatypes.ColorType | None = None,
    ):
        self.css[":root"][f"--md-admonition-icon--{name}"] = self.css.wrap_svg(data)
        header_color_str = helpers.get_color_str(header_color)
        icon_color_str = helpers.get_color_str(icon_color or (255, 255, 255))
        border_color_str = helpers.get_color_str(border_color or (255, 255, 255))
        self.css.add_rule(
            f".md-typeset .admonition.{name}, .md-typeset details.{name}",
            {
                "border-color": border_color_str,
            },
        )
        self.css.add_rule(
            f".md-typeset .{name} > .admonition-title, .md-typeset .{name} > summary",
            {"background-color": header_color_str},
        )
        self.css.add_rule(
            f".md-typeset .{name} > .admonition-title::before, .md-typeset .{name} >"
            " summary::before",
            {
                "background-color": icon_color_str,
                "-webkit-mask-image": f"var(--md-admonition-icon--{name})",
                "mask-image": f"var(--md-admonition-icon--{name})",
            },
        )

    def set_primary_foreground_color(
        self,
        color: datatypes.ColorType,
        light_shade: datatypes.ColorType | None = None,
        dark_shade: datatypes.ColorType | None = None,
    ):
        self._foreground_color = color
        self.set_color("primary", "custom")
        if light_shade is None:
            light_shade = color
        if dark_shade is None:
            dark_shade = color
        color_str = helpers.get_color_str(color)
        self.css[":root"]["--md-primary-fg-color"] = color_str
        self.css[":root"]["--md-primary-fg-color--light"] = helpers.get_color_str(
            light_shade,
        )
        self.css[":root"]["--md-primary-fg-color--dark"] = helpers.get_color_str(
            dark_shade,
        )
        return color_str

    def set_default_icon(self, icon_type: IconTypeStr, data: str):
        typ = ICON_TYPE[icon_type]
        self.css[":root"][f"--{typ}"] = self.css.wrap_svg(data)

    def add_status_icon(self, name: str, data: str):
        self.css[":root"][f"--md-status--{name}"] = self.css.wrap_svg(data)
        self.css.add_rule(
            f".md-status--{name}:after",
            {
                "-webkit-mask-image": f"var(--md-status--{name})",
                "mask-image": f"var(--md-status--{name})",
            },
        )

    def show_annotation_numbers(self):
        self.css.add_rule(
            ".md-typeset .md-annotation__index > ::before",
            {"content": "attr(data-md-annotation-id)"},
        )
        self.css.add_rule(
            ".md-typeset :focus-within > .md-annotation__index > ::before",
            {"transform": "none"},
        )

    def adapt_extensions(self, extensions: MutableMapping[str, dict]):
        for k in dict(extensions).copy():
            if k == "pymdownx.emoji":
                from materialx import emoji

                extensions[k].update(
                    {
                        "emoji_index": emoji.twemoji,
                        "emoji_generator": emoji.to_svg,
                    },
                )
            elif k in ["pymdownx.blocks.tab", "pymdownx.tabbed"]:
                extensions[k]["alternate_style"] = True
            elif k == "pymdownx.tasklist":
                extensions[k]["custom_checkbox"] = True


if __name__ == "__main__":
    theme = build_badge("palette", "tst")
    print(theme)
