import glob
import CaptchaCracker as cc

#이미지 학습
def learn_img():
    img_path_list = glob.glob(r'C:\Users\ChanYoungPark\Desktop\macro_test\sample\*.png')    #학습 데이터 이미지 경로 (파일명이 숫자와 같아야함)
    img_width = 130 #이미지 넓이
    img_height = 35 #이미지 높이
    CM = cc.CreateModel(img_path_list, img_width, img_height)   #학습모델 생성
    model = CM.train_model(epochs=130)  #반복 학습 시작
    model.save_weights('./test_weights2.h5')    #학습 결과 가중치 저장
    
    
    
learn_img()