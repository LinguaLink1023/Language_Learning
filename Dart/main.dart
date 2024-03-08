
void main() {
  // 先打开第4位，再打开第1位
  var number = 0x00;
  var mask = 0x08;
  number |= mask;
  mask >>=  3;
  assert(mask == 0x01);
  number |= mask;
  assert(number == 0x09);
}