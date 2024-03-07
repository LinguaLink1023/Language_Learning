import "dart:io";
import "dart:typed_data";

void main() {
  var number = 0xf0;
  var complementNumber = ~number;
  print(complementNumber);  
}