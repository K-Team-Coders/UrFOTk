from ultralytics import YOLO
import cv2
import os

# Словарь классов объектов
class_names = [
    "birth", "date_exec", "education", "f_name", "family", "name", "profi", "tk_num"
]

# Загрузите модель YOLOv8
model = YOLO(r"C:\Users\J\Desktop\rzd_hack\models\best.pt")

# Загрузите изображение
image_path = r'C:\Users\J\Desktop\rzd_hack\data\9\4014906_1024x768_1488595540vkladysh-oblozhka.jpg'
image = cv2.imread(image_path)

# Выполните детектирование объектов
results = model(image)

# Инициализируем словарь для сохранения координат
detected_objects = {class_name: [] for class_name in class_names}

# Создайте папку для сохранения обрезанных изображений, если она не существует
output_dir = 'segment'
os.makedirs(output_dir, exist_ok=True)

# Извлеките координаты детектируемых объектов и их классы
for idx, result in enumerate(results[0].boxes):
    # Координаты ограничивающей рамки
    x1, y1, x2, y2 = result.xyxy[0].numpy()
    
    # Класс детектированного объекта
    cls_id = int(result.cls[0])
    cls_name = class_names[cls_id]
    
    # Уверенность детектирования
    confidence = result.conf[0]
    
    print(f'Object Class: {cls_name}, Confidence: {confidence:.2f}')
    print(f'Bounding Box: ({x1}, {y1}), ({x2}, {y2})')
    
    # Сохраните координаты в словарь
    detected_objects[cls_name].append({
        'bounding_box': (x1, y1, x2, y2),
        'confidence': confidence
    })
    
    # Нарисуйте ограничивающую рамку на изображении (опционально)
    cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    # cv2.putText(image, f'{cls_name} ({confidence:.2f})', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Обрезаем соответствующую область изображения
    cropped_image = image[int(y1):int(y2), int(x1):int(x2)]
    
    # Сохраняем обрезанное изображение в папку segment
    cropped_image_path = os.path.join(output_dir, f'{cls_name}_{idx}.jpg')
    cv2.imwrite(cropped_image_path, cropped_image)

# Сохраните или покажите изображение с детектированными объектами
cv2.imwrite('output.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Выводим словарь с координатами
print(detected_objects)
