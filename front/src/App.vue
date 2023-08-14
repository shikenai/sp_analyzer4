<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import GeneralSettings from './components/GeneralSettings.Vue'
import axios from "axios";
import {ref} from "vue";

const testJson = ref('')
const test = () => {
  axios.get('api/test.json').then(res => {
    console.log('res')
    console.log(res)
    console.log('res.data.key1')
    console.log(res.data.key1)
    console.log('res.data.key1.value1A')
    console.log(res.data.key1.value1A)
    console.log('----')
    testJson.value = JSON.parse(res.data.key1)
    console.log(testJson)
    console.log(testJson.value)
  })
}


</script>

<template>
  <div id="wrapper">
    <nav>
      <ul>
        <li><a href="http://localhost:8000/admin/">管理画面</a></li>
        <li><a href="api/general_settings">設定一般</a></li>
        <li>3</li>
        <li>4</li>
        <li>5</li>
      </ul>
    </nav>
    <div id="contents">
        <div id="main"></div>
          <GeneralSettings></GeneralSettings>
        <div id="left"></div>
        <div id="right"></div>
    </div>

  </div>
</template>

<style scoped>
#wrapper {
  width: 1000px;
  height: 800px;
  background-color: white;
}
nav {
  background-color: antiquewhite;
  border: white solid 2px;
  width: auto;
  text-align: center;
}
/*#wrapper {*/
/*  border: red 3px solid;*/
/*  !*width: auto;*!*/
/*  !*height: 100%;*!*/
/*  !*padding: 0;*!*/
/*  !*margin: 0;*!*/
/*}*/

/*nav {*/
/*  text-align: center;*/
/*  height: 60px;*/
/*  border: #1a1a1a 1px solid;*/
/*}*/

nav ul {
  /*vertical-align: middle;*/
}

nav ul li {
  border: blue 1px dot-dash;
  list-style: none;
  display: inline-block;

  width: 18%;
  min-width: 90px;
}

/*nav ul li a {*/
/*  text-decoration: none;*/
/*  color: #333;*/
/*}*/

/*nav ul li.current a {*/
/*  color: #F33135;*/
/*}*/

/*nav ul li a:hover {*/
/*  color: #E7DA66;*/
/*}*/

/*#contents {*/
/*  display: flex;*/
/*  flex-direction: row;*/
/*  height: 800px;*/
/*}*/

/*#left {*/
/*  flex: 1;*/
/*  border: blueviolet solid 3px;*/
/*  overflow-x: scroll;*/
/*  white-space: nowrap;*/
/*}*/

/*#left p {*/
/*  margin: 0;*/
/*  padding-left: 5px;*/
/*}*/

/*#left ul {*/
/*  margin-top: 0;*/
/*  padding-top: 0;*/
/*}*/

/*#main {*/
/*  flex: 2;*/
/*  border: #E7DA66 solid 2px;*/
/*}*/

/*#right {*/
/*  flex: 1;*/
/*  border: green solid 1px;*/
/*}*/

/*.styled {*/
/*  border: 0;*/
/*  line-height: 2.5;*/
/*  padding: 0 20px;*/
/*  font-size: 1rem;*/
/*  text-align: center;*/
/*  color: #fff;*/
/*  text-shadow: 1px 1px 1px #000;*/
/*  border-radius: 10px;*/
/*  background-color: rgba(220, 0, 0, 1);*/
/*  background-image: linear-gradient(to top left, rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0.2) 30%, rgba(0, 0, 0, 0));*/
/*  box-shadow: inset 2px 2px 3px rgba(255, 255, 255, 0.6), inset -2px -2px 3px rgba(0, 0, 0, 0.6);*/
/*}*/

/*.styled:hover {*/
/*  background-color: rgba(255, 0, 0, 1);*/
/*}*/

/*.styled:active {*/
/*  box-shadow: inset -2px -2px 3px rgba(255, 255, 255, 0.6), inset 2px 2px 3px rgba(0, 0, 0, 0.6);*/
/*}*/
</style>
