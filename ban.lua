if matches[1]:lower() == 'ban' then-- /ban 
    if type(msg.reply_id)~="nil" and is_momod(msg) then
      if is_admin(msg) then
        local msgr = get_message(msg.reply_id,ban_by_reply_admins, false)
      else
        msgr = get_message(msg.reply_id,ban_by_reply, false)
      end
    end
      local user_id = matches[2]
      local chat_id = msg.to.id
      if string.match(matches[2], '^%d+$') then
        if tonumber(matches[2]) == tonumber(our_id) then 
         	return
        end
        if not is_admin(msg) and is_momod2(matches[2], msg.to.id) then
          	return "you can't ban mods/owner/admins"
        end
        if tonumber(matches[2]) == tonumber(msg.from.id) then
          	return "You can't ban your self !"
        end
        local name = user_print_name(msg.from)
        savelog(msg.to.id, name.." ["..msg.from.id.."] baned user ".. matches[2])
        ban_user(user_id, chat_id)
      else
		local cbres_extra = {
		chat_id = msg.to.id,
		get_cmd = 'ban',
		from_id = msg.from.id
		}
		local username = matches[2]
		local username = string.gsub(matches[2], '@', '')
		res_user(username, kick_ban_res, cbres_extra)
    	end
  end


  if matches[1]:lower() == 'unban' then -- /unban 
    if type(msg.reply_id)~="nil" and is_momod(msg) then
      local msgr = get_message(msg.reply_id,unban_by_reply, false)
    end
      local user_id = matches[2]
      local chat_id = msg.to.id
      local targetuser = matches[2]
      if string.match(targetuser, '^%d+$') then
        	local user_id = targetuser
        	local hash =  'banned:'..chat_id
        	redis:srem(hash, user_id)
        	local name = user_print_name(msg.from)
        	savelog(msg.to.id, name.." ["..msg.from.id.."] unbaned user ".. matches[2])
        	return 'کاربر '..user_id..' از بن خارج شد'
      else
		local cbres_extra = {
			chat_id = msg.to.id,
			get_cmd = 'unban',
			from_id = msg.from.id
		}
		local username = matches[2]
		local username = string.gsub(matches[2], '@', '')
		res_user(username, kick_ban_res, cbres_extra)
	end
 end

if matches[1]:lower() == 'kick' then
    if type(msg.reply_id)~="nil" and is_momod(msg) then
      if is_admin(msg) then
        local msgr = get_message(msg.reply_id,Kick_by_reply_admins, false)
      else
        msgr = get_message(msg.reply_id,Kick_by_reply, false)
      end
    end

	if string.match(matches[2], '^%d+$') then
		if tonumber(matches[2]) == tonumber(our_id) then 
			return
		end
		if not is_admin(msg) and is_momod2(matches[2], msg.to.id) then
			return " شما قادر به حذف این موارد نیستید mods/owner/admins "
		end
		if tonumber(matches[2]) == tonumber(msg.from.id) then
			return "You can't kick your self !"
		end
      		local user_id = matches[2]
      		local chat_id = msg.to.id
		name = user_print_name(msg.from)
		savelog(msg.to.id, name.." ["..msg.from.id.."] kicked user ".. matches[2])
		kick_user(user_id, chat_id)
	else
		local cbres_extra = {
			chat_id = msg.to.id,
			get_cmd = 'kick',
			from_id = msg.from.id
		}
		local username = matches[2]
		local username = string.gsub(matches[2], '@', '')
		res_user(username, kick_ban_res, cbres_extra)
	end
end


  if not is_admin(msg) then
    return
  end

  if matches[1]:lower() == 'banall' then -- Global ban
    if type(msg.reply_id) ~="nil" and is_admin(msg) then
      return get_message(msg.reply_id,banall_by_reply, false)
    end
    local user_id = matches[2]
    local chat_id = msg.to.id
      local targetuser = matches[2]
      if string.match(targetuser, '^%d+$') then
        if tonumber(matches[2]) == tonumber(our_id) then
         	return false 
        end
        	banall_user(targetuser)
       		return 'کاربر ['..user_id..' ] از همه ی گروه ها بن شد'
      else
	local cbres_extra = {
		chat_id = msg.to.id,
		get_cmd = 'banall',
		from_id = msg.from.id
	}
		local username = matches[2]
		local username = string.gsub(matches[2], '@', '')
		res_user(username, kick_ban_res, cbres_extra)
      	end
  end
  if matches[1]:lower() == 'unbanall' then -- Global unban
    local user_id = matches[2]
    local chat_id = msg.to.id
      if string.match(matches[2], '^%d+$') then
        if tonumber(matches[2]) == tonumber(our_id) then 
          	return false 
        end
       		unbanall_user(user_id)
        	return 'کاربر ['..user_id..' ] از همه ی گروه ها آنبن شد'
      else
	local cbres_extra = {
		chat_id = msg.to.id,
		get_cmd = 'unbanall',
		from_id = msg.from.id
	}
		local username = matches[2]
		local username = string.gsub(matches[2], '@', '')
		res_user(username, kick_ban_res, cbres_extra)
      end
  end
  if matches[1]:lower() == "gpbanlist" then -- Global ban list
    return لیست افراد بن شده از همه ی گروه ها()
  end
end

return {
  patterns = {
    "^([Bb]anall) (.*)$",
    "^([Bb]anall)$",
    "^([Bb]anlist) (.*)$",
    "^([Bb]anlist)$",
    "^([Gg]banlist)$",
    "^([Bb]an) (.*)$",
    "^([Kk]ick)$",
    "^([Uu]nban) (.*)$",
    "^([Uu]nbanall) (.*)$",
    "^([Uu]nbanall)$",
    "^([Kk]ick) (.*)$",
    "^([Kk]ickme)$",
    "^([Bb]an)$",
    "^([Uu]nban)$",
    "^([Ii]d)$",
    "^!!tgservice (.+)$"
  },
  run = run,
  pre_process = pre_process
}
