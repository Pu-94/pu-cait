module.exports = async ({ github, context, core }, { webhook, message }) => {
  const { ISSUE_NUMBER, REPO, OWNER } = process.env;
  const issueLink = `https://github.com/${OWNER}/${REPO}/issues/${ISSUE_NUMBER}`;
  
  try {
    await fetch(webhook, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        content: `${message}\n${issueLink}`,
        embeds: [{
          color: 0xff9900,
          fields: [{
            name: '处理命令',
            value: '`/approve [备注]` 或 `/reject [理由]`'
          }]
        }]
      })
    });
  } catch (error) {
    core.setFailed(`通知失败: ${error.message}`);
  }
};