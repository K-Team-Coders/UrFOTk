from transformers import AutoModel, AutoTokenizer


def save_model(model_name, save_directory):
    """
    Функция для сохранения модели и токенизатора в указанный каталог.

    :param model_name: Имя или путь до модели на Hugging Face Hub.
    :param save_directory: Путь до каталога, где будет сохранена модель.
    """
    # Загрузка модели и токенизатора
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Сохранение модели и токенизатора
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)

    print(f"Model and tokenizer saved to {save_directory}")


# Пример использования функции
model_name = 'ai-forever/ReadingPipeline-notebooks'  # замените на имя вашей модели
save_directory = './model2'  # замените на нужный вам путь

save_model(model_name, save_directory)
model_name = 'ai-forever/ReadingPipeline-Peter'  # замените на имя вашей модели
save_directory = './model1'  # замените на нужный вам путь

save_model(model_name, save_directory)
