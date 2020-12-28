from PIL import Image

image = Image.open('./in1.jpg')
resize_image = image.resize((650,460))
resize_image.save('./in11.jpg')