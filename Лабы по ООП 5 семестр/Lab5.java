// 4. Создайте класс на Java со статическими полями и
// методами. Инициализируйте статические поля в статическом
// блоке инициализации.
public class Lab5 {
    public static class FiguresSquare {
        public static double PI;

        public static boolean is_negative(int num) {
            return num < 0;
        }

        public static double CircleSquare(int radius) {
            if (is_negative(radius)) {
                return -0.1;
            }

            return PI * (radius * radius);
        }

        public static int Square(int side) {
            if (is_negative(side)) {
                return -1;
            }

            return side * side;
        }

        public static double DiamCircleSquare(int diam) {
            if (is_negative(diam)) {
                return -1;
            }

            return 4 * PI * (diam * diam);
        }

        static { /* статический блок инициализации */
            PI = 3.14;
        }
    }

    public static void main(String[] args) {
        int radius = 20;
        int side = 5;
        int diam = 40;
        System.out.println("Площадь круга с радиусом " + radius + " = " + FiguresSquare.CircleSquare(radius));
        System.out.println("Площадь круга с диаметром " + diam + " = " + FiguresSquare.DiamCircleSquare(10));
        System.out.println("Площадь квадрата со стороной " + side + " = " + FiguresSquare.Square(side));
    }
}