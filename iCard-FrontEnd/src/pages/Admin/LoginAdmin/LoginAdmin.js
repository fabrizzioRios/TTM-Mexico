import React from 'react'
import "./LoginAdmin.scss"
import { LoginForm } from '../../../components/Admin'

export function LoginAdmin() {
  return (
    <div className={'login-admin'}>
      <div className={'login-admin-content'}>
        <h1>TTM Mexico Login Admin</h1>
        <LoginForm />
      </div>
    </div>
  )
}
