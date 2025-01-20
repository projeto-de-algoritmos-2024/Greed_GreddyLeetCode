class Solution:
    def scheduleCourse(self, courses):
        # Ordenar os cursos pelo prazo (lastDay)
        courses.sort(key=lambda x: x[1])

        current_time = 0
        selected_courses = []

        for duration, lastDay in courses:
            if current_time + duration <= lastDay:
                # Se o curso puder ser concluído dentro do prazo, adiciona
                selected_courses.append((duration, lastDay))
                current_time += duration
            else:
                # Remover o curso mais longo para encaixar o atual, se necessário
                if selected_courses and duration < max(selected_courses, key=lambda x: x[0])[0]:
                    longest_course = max(selected_courses, key=lambda x: x[0])
                    selected_courses.remove(longest_course)
                    current_time -= longest_course[0]
                    selected_courses.append((duration, lastDay))
                    current_time += duration

        return len(selected_courses)
