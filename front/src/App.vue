<template>
  <div id="nav">
    <router-link to="/">Home </router-link>|
    <router-link to="/about">About </router-link>|   
    <router-link to="/alignments">Alinear</router-link>|
    <router-link to="/sequences/add">Añadir nueva secuencia</router-link>|
    <router-link to="/sequences/<id>">Editar secuencia</router-link>
  </div>
  <router-view />
</template>
