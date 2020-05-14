<template>
  <div id="employee-table">
    <p v-if="employees.length === 0">There is no employee.</p>
    <table v-else>
      <thead>
        <tr>
          <th>Employee name</th>
          <th>Employee email</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="employee in employees" :key="employee.id">
          <td v-if="editing === employee.id">
            <input type="text" v-model="employee.name" />
          </td>
          <td v-else>{{ employee.name }}</td>
          <td v-if="editing === employee.id">
            <input type="text" v-model="employee.email" />
          </td>
          <td v-else>{{ employee.email }}</td>
          <td v-if="employee.id === editing">
            <button @click="editEmployee(employee)">Save</button>
            <button @click="cancelEdit(employee)">Cancel</button>
          </td>
          <td v-else>
            <button @click="editMode(employee)">Edit</button>
            <button @click="$emit('delete:employee', employee.id)">
              Delete
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "employee-table",
  data() {
    return {
      editing: null,
      cachedEmployee: null
    };
  },
  props: {
    employees: Array
  },
  methods: {
    editMode(employee) {
      this.cachedEmployee = Object.assign({}, employee);
      this.editing = employee.id;
    },
    editEmployee(employee) {
      if (employee.name === "" || employee.email === "") return;
      this.$emit("edit:employee", employee, employee.id);
      this.editing = null;
    },
    cancelEdit(employee) {
      Object.assign(employee, this.cachedEmployee);
      this.editing = null;
    }
  }
};
</script>

<style scoped>
button {
  margin: 0 0.5rem 0 0;
}
</style>
