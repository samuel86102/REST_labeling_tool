# REST Labeling Tool

## 使用說明
### 1. 前置作業
1. 解壓縮REST_labeling_tool
2. 於電腦中安裝Python（使用版本：Python 3.11.1 - Dec. 6, 2022）與Visual Studio Code（使用版本：1.76.0 (Universal)）
3. 於terminal輸入套件安裝指令(見2. 套件安裝)，系統將自動安裝本操作所需package。註：pip具版本限制，python安裝之時便為附屬安裝檔，視安裝版本需將指令變更ex.（pip/pip3）。
4. 樣點偵測三角形：使用adobe photoshop 2023 套疊XnViewMP所繪製20\*20格線之自動相機照片截圖，參考各樣點自動相機偵測最遠距離、最寬角度繪製偵測三角形（red，5pt）。註：輸出尺寸為2048*1440像素（需符合自動相機檔案尺寸），檔名為mark.jpg。
5. 將待偵測樣區之自動相機照片複製至images資料夾，須符合副檔名為.jpg/.JPG/.jpeg/.JPEG。

### 2. 套件安裝
```python
pip install pillow
pip install matplotlib
pip install numpy
pip install pandas
```

### 3. 使用程式

1. 以terminal開啟`main.py`，系統將自動開啟images中之照片與偵測三角形（mark.jpg）合併。Terminal需手動輸入3個label作為標記，分別為：
   1. label1出現個體,0=否,1=是
   2. label2第一張與否,0=否,1=是
   3. label3出現單/複數,0=單數,1=複數
輸入enter後將自動開啟下一張圖片，直至偵測完畢。
2. 系統將自動辨識images中之與偵測三角形（mark.jpg）合併後輸出疊圖照片至merge資料夾。
3. 系統自動輸出偵測結果之.csv檔案，首欄依序為：隨機生成id、副資料夾名稱、相片檔名、日期、時間、辨認結果、觸發序號、停留時長。




---



## User Instructions
### 1. Prerequisites
1. Unzip the REST_labeling_tool folder.
2. Install Python on your computer (using version: Python 3.11.1 - Dec. 6, 2022) and Visual Studio Code (using version: 1.76.0 (Universal)).
3. In the terminal, execute the package installation commands (see 2. Package Installation), and the system will automatically install the required packages for this operation. Note: Depending on the installation, you might need to use pip or pip3.
4. For detecting sample points in a triangle: Use Adobe Photoshop 2023 to overlay XnViewMP and draw a 20x20 grid on the automatic camera screenshot. Reference the farthest distance and widest angle of each sample point to draw the detection triangle (red, 5pt). Note: The output size should be 2048x1440 pixels (matching the automatic camera file's dimensions) and the filename should be mark.jpg.
5. Copy the automatic camera photos of the areas to be detected into the "images" folder, with file extensions .jpg/.JPG/.jpeg/.JPEG.

### 2. Package Installation
```python
pip install pillow
pip install matplotlib
pip install numpy
pip install pandas
```

### 3. How to Use the Program

1. Open `main.py` in the terminal, and the system will automatically display the merged photo of the images along with the detection triangle (mark.jpg). Manually enter three labels in the terminal as follows:
   1. label1: Presence of individuals, 0=No, 1=Yes
   2. label2: First appearance, 0=No, 1=Yes
   3. label3: Singular/Plural, 0=Singular, 1=Plural
   After entering, press Enter, and the next image will be automatically displayed, until the detection is completed.
2. The system will automatically recognize the merged photo of the images with the detection triangle (mark.jpg) and output it to the "merge" folder.
3. The system will automatically generate a .csv file with the detection results. The first column contains: randomly generated ID, subfolder name, photo filename, date, time, recognition result, trigger number, and duration of stay.
