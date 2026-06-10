.auth-shell {
  min-height: 100vh;
  display: grid;
  place-items: center;
  padding: 32px;
  background: radial-gradient(circle at top, rgba(99,102,241,0.14), transparent 25%),
              linear-gradient(180deg, #0B1020 0%, #070B16 100%);
}

.auth-card {
  width: min(520px, 100%);
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 32px;
  box-shadow: var(--shadow);
  padding: 40px;
}

.auth-card h1 {
  margin-top: 0;
  margin-bottom: 12px;
  font-size: 2rem;
  font-weight: 700;
}

.auth-card p {
  margin: 0 0 28px;
  color: var(--muted);
}

.form-grid {
  display: grid;
  gap: 18px;
}

.action-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.radio-group {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.radio-group input {
  width: auto;
}

.auth-note {
  margin-top: 16px;
  font-size: 0.95rem;
  color: var(--muted);
}

.auth-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 24px;
  flex-wrap: wrap;
  gap: 12px;
}

.auth-footer a {
  color: var(--accent);
}

.auth-error,
.auth-success {
  border-radius: 14px;
  padding: 14px 16px;
  margin-bottom: 18px;
  font-size: 0.95rem;
}

.auth-error {
  background: rgba(239,68,68,0.14);
  border: 1px solid rgba(239,68,68,0.22);
  color: #FECACA;
}

.auth-success {
  background: rgba(34,197,94,0.14);
  border: 1px solid rgba(34,197,94,0.22);
  color: #D1FAE5;
}
