import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/campus",
    name: "Campus",
    component: () => import("../views/Campus.vue")
  },
  {
    path: "/major",
    name: "Major",
    component: () => import("../views/Major.vue")
  },
  {
    path: "/person",
    name: "Person",
    component: () => import("../views/Person.vue")
  },
  {
    path: "/teacher",
    name: "Teacher",
    component: () => import("../views/Teacher.vue")
  },
  {
    path: "/student",
    name: "Student",
    component: () => import("../views/Student.vue")
  },
  {
    path: "/student_status_change",
    name: "Course",
    component: () => import("../views/StudentStatusChange.vue")
  },
  {
    path: "/class",
    name: "Class",
    component: () => import("../views/Class.vue")
  },
  {
    path: "/course",
    name: "Course",
    component: () => import("../views/Course.vue")
  },
  {
    path: "/course_info",
    name: "Course",
    component: () => import("../views/CourseInfo.vue")
  },
  {
    path: "/course_selection",
    name: "CourseSelection",
    component: () => import("../views/CourseSelection.vue")
  },
];

const router = new VueRouter({
  routes
});

export default router;
