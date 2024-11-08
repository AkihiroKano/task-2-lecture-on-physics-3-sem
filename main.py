import numpy as np
import matplotlib.pyplot as plt

# Константы
GRAVITY = 9.81  # Ускорение свободного падения, м/с^2

# Функция для расчета траектории
def compute_trajectory(initial_height, initial_velocity, launch_angle):
    # Конвертация угла в радианы
    angle_rad = np.radians(launch_angle)

    # Время подъема к вершине
    time_to_peak = initial_velocity * np.sin(angle_rad) / GRAVITY

    # Максимальная высота и время падения
    peak_height = initial_height + (initial_velocity * np.sin(angle_rad)) ** 2 / (2 * GRAVITY)
    time_to_fall = np.sqrt(2 * peak_height / GRAVITY)

    # Общее время движения
    total_time = 2 * time_to_peak + time_to_fall

    # Период времени для построения
    time_values = np.linspace(0, total_time, num=500)

    # Координаты движения
    x_coords = initial_velocity * np.cos(angle_rad) * time_values
    y_coords = initial_height + initial_velocity * np.sin(angle_rad) * time_values - 0.5 * GRAVITY * time_values ** 2

    # Фильтрация положительных значений y
    valid_points = y_coords >= 0
    time_values = time_values[valid_points]
    x_coords = x_coords[valid_points]
    y_coords = y_coords[valid_points]

    return time_values, x_coords, y_coords

# Функция для расчета текущей скорости
def compute_velocity(initial_velocity, launch_angle, time_values):
    angle_rad = np.radians(launch_angle)
    horizontal_velocity = initial_velocity * np.cos(angle_rad)
    vertical_velocity = initial_velocity * np.sin(angle_rad) - GRAVITY * time_values
    resultant_velocity = np.sqrt(horizontal_velocity ** 2 + vertical_velocity ** 2)
    return resultant_velocity

# Визуализация результатов
def plot_motion(initial_height, initial_velocity, launch_angle):
    # Траектория
    time_values, x_coords, y_coords = compute_trajectory(initial_height, initial_velocity, launch_angle)

    # Скорость
    velocity_values = compute_velocity(initial_velocity, launch_angle, time_values)

    # Построение графиков
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    # График траектории
    axs[0].plot(x_coords, y_coords)
    axs[0].set_title('Траектория движения объекта')
    axs[0].set_xlabel('Горизонтальное положение, м')
    axs[0].set_ylabel('Вертикальное положение, м')

    # Графики зависимости координат от времени
    axs[1].plot(time_values, x_coords, label='Положение x(t)')
    axs[1].plot(time_values, y_coords, label='Положение y(t)')
    axs[1].set_title('Зависимость координат от времени')
    axs[1].set_xlabel('Время, с')
    axs[1].set_ylabel('Координаты, м')
    axs[1].legend()

    # График зависимости скорости от времени
    axs[2].plot(time_values, velocity_values)
    axs[2].set_title('Скорость в зависимости от времени')
    axs[2].set_xlabel('Время, с')
    axs[2].set_ylabel('Скорость, м/с')

    # Показ графиков
    plt.tight_layout()
    plt.show()

# Основная программа
if __name__ == '__main__':
    # Ввод начальных параметров
    initial_height = float(input("Введите начальную высоту (м): "))
    initial_velocity = float(input("Введите начальную скорость (м/с): "))
    launch_angle = float(input("Введите угол запуска (градусы): "))

    # Построение графиков
    plot_motion(initial_height, initial_velocity, launch_angle)
