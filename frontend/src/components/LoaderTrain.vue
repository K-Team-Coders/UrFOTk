<template>
  <div class="">
    <div class="container">
      <div class="track"></div>
      <div class="train"></div>
    </div>
  </div>
</template>
<style scoped>
body {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.container {
  position: relative;
}

.track {
  position: relative;
  overflow: hidden;
  width: 50px;
  height: 100px;
  border-left: 3px solid #333;
  transform: skew(-10deg) rotateX(45deg);
}

.track:before {
  content: "";
  position: absolute;
  height: 3px;
  width: 50px;
  background-color: #333;
  top: 90px;
  box-shadow: 0 0 #333, 0 -10px #333, 0 -20px #333, 0 -30px #333, 0 -40px #333,
    0 -50px #333, 0 -50px #333, 0 -60px #333, 0 -70px #333, 0 -80px #333,
    0 -90px #333, 0 -100px #333, 0 -110px #333, 0 -120px #333, 0 -130px #333,
    0 -140px #333;
  animation: track 1s linear infinite;
}

@keyframes track {
  0% {
    transform: translateY(70px) rotateX(45deg);
  }
  100% {
    transform: translateY(0px) rotateX(45deg);
  }
}

.track:after {
  content: "";
  position: absolute;
  transform: rotate(-15deg);
  width: 50px;
  height: 120px;
  background-color: #fff;
  border-left: 3px solid #333;
  left: 35px;
  top: -10px;
}

.train {
  position: absolute;
  width: 60px;
  height: 60px;
  background-color: #333;
  border-radius: 15px;
  top: 0;
  left: 0px;
  transform-origin: bottom;
  animation: rotate 1s linear infinite;
}

.train:before {
  content: "";
  position: absolute;
  background-color: #ced4da;
  width: 20px;
  height: 15px;
  left: 9px;
  top: 15px;
  box-shadow: 22px 0 #ced4da;
}

.train:after {
  content: "";
  position: absolute;
  background-color: #ced4da;
  border-radius: 50%;
  height: 10px;
  width: 10px;
  top: 45px;
  left: 10px;
  box-shadow: 30px 0px #ced4da;
}

@keyframes rotate {
  0% {
    transform: rotate(0);
  }
  25% {
    transform: rotate(2deg);
  }
  50% {
    transform: rotate(0);
  }
  75% {
    transform: rotate(-2deg);
  }
  100% {
    transform: rotate(0);
  }
}
</style>
