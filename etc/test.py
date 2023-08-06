import glob
import CaptchaCracker as cc

#이미지 학습
def learn_img():
    img_path_list = glob.glob(r'C:\Users\ChanYoungPark\Desktop\web\sample\*.png')    #학습 데이터 이미지 경로 (파일명이 숫자와 같아야함)
    img_width = 130 #이미지 넓이
    img_height = 35 #이미지 높이
    CM = cc.CreateModel(img_path_list, img_width, img_height)   #학습모델 생성
    model = CM.train_model(epochs=100)  #반복 학습 시작
    model.save_weights('./test_weights.h5')    #학습 결과 가중치 저장



# 결과 도출
def result_img():
    target_img_path = './isT.png'    #타켓 이미지 경로
    img_width = 130 #타켓 이미지 넓이
    img_height = 35 #타켓 이미지 높이
    img_length = 6  #타켓 이미지가 포함한 문자 수
    img_char = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}   #타켓 이미지안에 포함된 문자들
    weights_path = './test_weights.h5' #학습 결과 가중치 경로
    AM = cc.ApplyModel(weights_path, img_width, img_height, img_length, img_char)   #결과 가중치를 가지는 모델 생성
    pred = AM.predict(target_img_path)  #결과 도출
    return pred



print(result_img())