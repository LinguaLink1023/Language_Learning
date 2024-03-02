import "dart:io";

void main() {
  print("Hello dart!\n");
  var name = "Jerry";
  var age = 39;
  var height = 100000000.81456 + 0.1;
  var height2 = height - 100000000.81456;
  print("Hello, I'm $name. I'm $age years old\n, my height is ${9 ~/ 7} cm");
  print("Please enter your wife's height: ");
  var myWifeHeight = stdin.readLineSync();
  print("My wife's height: ${myWifeHeight}");
}