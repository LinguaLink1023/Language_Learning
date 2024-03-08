import 'dart:math';

class Animal {}

class Dog extends Animal {
  void bark() => print("wang wang wang !");
  void sit_dowm() => print("sitted down!");
  void turn_left() => print("turned left!");
  void catch_ball() => print("catched");
}

class Cat extends Animal {
  void miao() => print("miao!miao!miao!");
}

Animal getAnimal() {
  var rgn = new Random();
  var number = rgn.nextInt(100);
  return number % 2 == 0 ? Dog() : Cat();
}

void main() {
  Animal someAnimal = getAnimal(); // 获得这个Animal，可能是Dog，也可能是Cat
  Dog jerry = Dog();
  jerry
    ..bark()
    ..sit_dowm()
    ..turn_left()
    ..catch_ball();
  if (someAnimal is Dog) {
    // 如果没做这个判断，将不能调用bark()
    someAnimal.bark();
    someAnimal.sit_dowm(); // 当然，这里的类型转换，没有必要，因为程序到这里已经判断出是Dog类型了
  } else if (someAnimal is Cat) {
    // 如果没做这个判断，将不能调用miao()
    someAnimal.miao();
  }
}
