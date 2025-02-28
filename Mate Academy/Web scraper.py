import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

class MateAcademyScraper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--log-level=3")

        self.driver = webdriver.Chrome(options=options)
        self.url = "https://mate.academy"
        self.course = ".ProfessionCard_title__m7uno"
        self.duration = ".ProfessionCard_duration__13PwX"
        self.description = ".ProfessionCard_description__K8weo"
        self.moduls = ".CourseModulesList_topicName__ZrDxT"
        self.topics = ".CourseModulesList_topicsCount__yAPxH"
        self.course_links = ".ProfessionCard_cardWrapper__BCg0O"

    def load_page(self, url):
        self.driver.get(url)
        self.driver.execute_script("""
                                document.querySelectorAll('*').forEach(el => {
                                    el.style.setProperty('opacity', '1', 'important');
                                });
                            """)

    def start(self):
        self.load_page(self.url)

    def scrape(self):
        data = self.extract_to_dict(
            course=self.course,
            duration=self.duration,
            description=self.description
        )
        list_href = self.extract_list_selectors(self.course_links)

        course_links = [link.get_attribute("href") for link in list_href]

        additional_data = {"modules": [], "topics": []}
        for link in course_links:
            print("Loading page...")
            self.load_page(link)

            modules =  [self.strip_elem(module) for module in  self.extract_list_selectors(self.moduls)]

            topics = self.find_selector(self.topics)

            additional_data["modules"].append(modules)
            additional_data["topics"].append(topics)
        data.update(additional_data)
        return data

    def extract_list_selectors(self, selector):
        return [element for element in self.driver.find_elements(By.CSS_SELECTOR, selector)]


    def find_selector(self, selector):
        try:
            return self.strip_elem(self.driver.find_element(By.CSS_SELECTOR, selector))
        except Exception as e:
            return f"Data not found {str(e)}"


    def extract_to_dict(self, **kwargs):
        return {key: [self.strip_elem(element) for element in self.driver.find_elements(By.CSS_SELECTOR, selector)] for key, selector in kwargs.items()}

    @staticmethod
    def save_to_csv( courses):
        if courses:
            df = pd.DataFrame(courses)
            df.to_csv("mate_academy_courses.csv", index=False, encoding="utf-8")
            print("Дані успішно збережені у 'mate_academy_courses.csv'!")
        else:
            print("Дані не були збережені, оскільки список курсів порожній.")

    @staticmethod
    def strip_elem(elem):
        return elem.text.strip()

    @staticmethod
    def print_courses(courses):
        if courses:
            for i in range(len(courses['course'])):
                print(f"Курс: {courses['course'][i]}")
                print(f"Тривалість: {courses['duration'][i]}")
                print(f"Модулі: {courses['modules'][i]}")
                print(f"Теми: {courses['topics'][i]}")
                print(f"Опис: {courses['description'][i]}\n")
        else:
            print("⚠ Немає курсів для відображення!")

    def close(self):
        """Закриває браузерну сесію."""
        self.driver.quit()



if __name__ == "__main__":
    scraper = MateAcademyScraper()
    print("Script in process...")
    scraper.start()
    course_data = scraper.scrape()
    scraper.print_courses(course_data)
    scraper.save_to_csv(course_data)
    scraper.close()
