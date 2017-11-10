int cols = 9;
int rows = 9;
int w, a, b, c;

int[][] num = {  
  {0, 9, 0, 0, 0, 0, 0, 0, 1}, 
  {0, 0, 8, 0, 0, 0, 9, 2, 3}, 
  {4, 0, 0, 0, 0, 2, 0, 6, 0}, 
  {0, 2, 0, 0, 0, 8, 0, 0, 4}, 
  {0, 7, 0, 5, 1, 6, 0, 8, 0}, 
  {8, 0, 0, 9, 0, 0, 0, 3, 6}, 
  {0, 6, 0, 4, 0, 0, 0, 0, 5}, 
  {1, 4, 9, 0, 0, 0, 6, 0, 0}, 
  {5, 0, 0, 0, 0, 0, 0, 4, 0}, 
};
int  numCopy[][] = {  
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0}, 
};


void setup() {
  size(900, 900);
  background(255);

  c = (cols+rows)/2;
  a = ((width+height)/2)/c;
  b = width / 100 + 1;
  w = ((width/rows)+(height/cols))/2;
}

int nx = 0;
int ny = 0;
int cN;
boolean checkRow;

void draw() {
  grid();
  drawNumbers();
  arrayCopy(num, numCopy);
  cN = getNum();
  // cN = 9;

  /* for (int i = 0; i < 9; i++) {
   checkRow = checkRow(ny, cN, i);
   }
   */
  // println("Row:   " + checkRow + "      current num    " + cN);
  // println("Current num: "+ cN +"    Row:" + checkRow + "    Coll:" + checkColl(ny, cN) + "    Square:" + checkSquare(nx, ny, cN));
  //println("Current num: "+ cN +"    Row:" + checkRow(ny, cN) + "    Coll:" + checkColl(ny, cN) + "    Square:" + checkSquare(nx, ny, cN));
  println("Check:   " + check(cN) + "      current num    " + cN);
}


int stW = 1;
void grid() {

  for (int i = 0; i < b*100; i+=100) {
    strokeWeight(stW);
    line(i, 0, i, 900);
    line(0, i, 900, i);
    if (i/100 == 2 || i/100 == 5 || i/100 == 8 || i/100 == 10) {
      stW = 5;
    } else {
      stW = 1;
    }
  }
}
color fC(int j, int i) {
  color fc;
  if (num[j][i] == numCopy[j][i]) {
    fc = color(255, 0, 0);
  } else {
    fc = color(0, 0, 0);
  }

  return fc;
}


void drawNumbers() {
  textSize(75);
  for (int i = 0; i <= c-1; i++) {
    for (int j = 0; j <= c-1; j++) {
      if (num[j][i] != 0) {
        fill(fC(j, i));
        text(num[j][i], (i*100+10), (j*100-10)+100);
      }
    }
  }
}
int idx = 0;
int getNum() {
  if (idx < 9) {
    idx++;
  } else {
    idx = 1;
  }
  return idx;
}
boolean check(int cN) {
  boolean bo = false;
  if (checkRow(ny, cN)&& checkColl(ny, cN)) {
    bo = true;
  }
  return bo;
}

boolean checkempty(int i, int j) {
  boolean empty = false;
  if (num[i][j] == 0) {
    empty = true;
  }
  return empty;
};

boolean checkRow(int nY, int cN) {
  boolean bo = false;
  //  println(c);
  for (int c = 0; c < 9; c++) {

    if (cN != num[nY][c]) {
      //println("arr     " + num[nY][c] + "      index    " + c);
      bo = true;
    } else if (cN == num[nY][c]) {
      bo = false;
    }
  }
  return bo;
};

boolean checkColl(int nX, int cN) {
  boolean bo = false;
  for (int c = 0; c < 9; c++) {

    if (cN == num[c][nX]) {
      bo = false;
    } else {
      bo = true;
    }
  }
  return bo;
};

int sq;
boolean checkSquare(int nX, int nY, int cn) {
  boolean bo = false;
  switch(sq) {
  case 1:
  case 2:
  case 3:
  case 4:
  case 5:
  case 6:
  case 7:
  case 8:
  case 9:
  }
  return bo;
};