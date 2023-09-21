import transfer_color as tc

def ladder_colors(html_color='#000000'):
    br, bg, bb = tc.html_to_rgb('#000000')
    r, g, b = tc.html_to_rgb(html_color)
    er, eg, eb = tc.html_to_rgb('#FFFFFF')
    ladder_color_list = []
    br_list = [tc.rgb_to_html(int(br + i * (r - br) /10),int(bg + i * (g - bg) /10),int(bb + i * (b - bb) /10)) for i in range(10)]
    er_list = [tc.rgb_to_html(int(r + (i+1) * (er - r) /10),int(g + (i+1) * (eg - g) /10),int(b + (i+1) * (eb - b) /10)) for i in range(10)]
    ladder_color_list.extend(br_list)
    ladder_color_list.append(html_color)
    ladder_color_list.extend(er_list)
    return ladder_color_list


def get_color(theme=None):
    color_list = ['#3366FF',
                  '#6AB520',
                  '#0CA6FF',
                  '#FFBF1E',
                  '#FF4E2B']
    return color_list



