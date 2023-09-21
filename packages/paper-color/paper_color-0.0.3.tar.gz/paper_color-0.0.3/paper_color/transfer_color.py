def html_to_rgb(html_color):
    if html_color.startswith('#'):
        html_color = html_color[1:]
    r = int(html_color[:2], 16)
    g = int(html_color[2:4], 16)
    b = int(html_color[4:], 16)
    return r, g, b


def rgb_to_html(r, g, b):
    r_hex = format(r, '02x')
    g_hex = format(g, '02x')
    b_hex = format(b, '02x')
    html_color = '#' + r_hex + g_hex + b_hex
    return html_color