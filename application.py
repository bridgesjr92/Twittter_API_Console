import dearpygui.dearpygui as dpg
from Twitter_class import Posted



def buttonclick(sender):
    Posted.post(dpg.get_value(x))
    print('tweet sent')
    dpg.set_value(x,'')


dpg.create_context()
dpg.create_viewport(title='Twitter_Terminal', width=600, height=400)

with dpg.window(label='Twitter', width=600, height=200):
    dpg.add_text("Lets Tweet My boy")
    x = dpg.add_input_text()
    y = dpg.add_button(label='send tweet', callback=buttonclick)





dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()



