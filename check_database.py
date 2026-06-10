function initSettingsPage() {
  if (!requireAuth()) return;
  loadSharedComponent('header', () => {
    setProfileSummary();
    bindHeaderActions();
  });
  initSidebar();
  const headerTitle = document.getElementById('page-title');
  if (headerTitle) headerTitle.textContent = 'Settings';
  populateSettings();
  bindSettingsSubmit();
}

async function populateSettings() {
  const response = await apiRequest('/settings', 'GET');
  const settings = response.settings || {};
  document.getElementById('app-name').value = settings.applicationName || 'SQL Migrator';
  document.getElementById('system-version').value = settings.version || '1.0.0';
  document.getElementById('maintenance-mode').checked = settings.maintenanceMode || false;
  document.getElementById('default-database').value = settings.defaultDatabase || 'PostgreSQL';
  document.getElementById('session-timeout').value = settings.sessionTimeout || 30;
  document.getElementById('password-policy').value = settings.passwordPolicy || 'Strong';
  document.getElementById('email-notifications').checked = settings.emailNotifications || true;
  document.getElementById('migration-alerts').checked = settings.migrationAlerts || true;

  const user = getUserInfo();
  if (user) {
    document.getElementById('profile-name').value = user.name;
    document.getElementById('profile-email').value = user.email;
  }
}

function bindSettingsSubmit() {
  const settingsForm = document.getElementById('settings-form');
  if (!settingsForm) return;
  settingsForm.addEventListener('submit', async (event) => {
    event.preventDefault();
    const payload = {
      applicationName: document.getElementById('app-name').value,
      version: document.getElementById('system-version').value,
      maintenanceMode: document.getElementById('maintenance-mode').checked,
      defaultDatabase: document.getElementById('default-database').value,
      sessionTimeout: parseInt(document.getElementById('session-timeout').value, 10),
      passwordPolicy: document.getElementById('password-policy').value,
      emailNotifications: document.getElementById('email-notifications').checked,
      migrationAlerts: document.getElementById('migration-alerts').checked,
    };
    await apiRequest('/settings', 'POST', payload);
    showNotification('Settings saved successfully', 'success');
  });
}
