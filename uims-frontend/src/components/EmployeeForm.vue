<template>
  <div id="employee-form">
    <form @submit.prevent="handleSubmit">
      <label>Employee name</label>
      <input
        ref="first"
        type="text"
        v-model="employee.name"
        :class="{ 'has-error': submitting && invalidName }"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <label>Employee Email</label>
      <input
        type="text"
        v-model="employee.email"
        :class="{ 'has-error': submitting && invalidEmail }"
        @focus="clearStatus"
        @keypress="clearStatus"
      />
      <p class="error-message" v-if="submitting && error">
        Please fill out all required fields
      </p>
      <p class="success-message" v-if="success">Employee successfully added</p>
      <button>Add Employee</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "employee-form",
  data() {
    return {
      submitting: false,
      error: false,
      success: false,
      employee: {
        name: "",
        email: ""
      }
    };
  },
  methods: {
    handleSubmit() {
      this.submitting = true;
      this.clearStatus();
      // console.log('testing handleSubmit');
      if (this.invalidName || this.invalidEmail) {
        this.error = true;
        return;
      }
      this.$emit("add:employee", this.employee);
      this.$refs.first.focus();
      this.employee = {
        name: "",
        email: ""
      };
      this.success = true;
      this.error = false;
      this.submitting = false;
    },
    clearStatus() {
      this.success = false;
      this.error = false;
    }
  },
  computed: {
    invalidName: function() {
      return this.employee.name === "";
    },
    invalidEmail: function() {
      return this.employee.email === "";
    }
  }
};
</script>

<style scoped>
form {
  margin-bottom: 2rem;
}

[class*="-message"] {
  font-weight: 500;
}

.error-message {
  color: #d33c40;
}

.success-message {
  color: #32a95d;
}
</style>
