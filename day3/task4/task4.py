# Напишите скрипт, который будет открывать лог, и выводить кол-во ошибок модуля
# Kernel: System: Ticket: TicketPermission за 6 августа с 10:00 до 18:00.
# Сгруппируйте все ошибки, и выведите их от большего кол-ва упоминаний к меньшему.
# Запишите данные в файлы, названия которых будет датой ошибки
# (example: 02.01.2017.txt, 02.02.2017.txt, 02.05.2017.txt)

import datetime
from operator import itemgetter

counter = 0
errors_count = {}

with open('otrs_error.log', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.split(']')
        line = [elem.strip('[') for elem in line]
        try:
            date = datetime.datetime.strptime(line[0], '%a %b %d %H:%M:%S %Y')
        except ValueError:
            pass
        else:
            d = str(date.date())

            if datetime.datetime(2017, 8, 6, 10) <= date <= datetime.datetime(2017, 8, 6, 18):
                if line[2] == 'Kernel::System::Ticket::TicketPermission':
                    counter += 1

            if d in errors_count.keys():
                if line[2] in errors_count[d].keys():
                    errors_count[d][line[2]] += 1
                else:
                    errors_count[d].update({line[2]: 1})
            else:
                errors_count.update({d: {line[2]: 1}})

    for k in errors_count.keys():
        errors_count[k] = sorted(list(zip(errors_count[k].keys(), errors_count[k].values())), key=itemgetter(1), reverse=True)

        with open('{}.txt'.format(datetime.datetime.strptime(k, '%Y-%m-%d').strftime('%d.%m.%Y')), 'w') as txt:
            data = ('\n'.join(['{}: {}'.format(errors_count[k][i][0], errors_count[k][i][1]) for i in range(len(errors_count[k]))]))
            txt.write(data)

    total = {}
    for branch in errors_count.values():
        for elem in branch:
            if elem[0] in total:
                total[elem[0]] += elem[1]
            else:
                total[elem[0]] = elem[1]

    sort_total = sorted(total, key=lambda i: total[i], reverse=True)
    print('Kernel:System:Ticket:TicketPermission: ', counter)
    print('\n'.join('{}: {}'.format(error, total[error]) for error in sort_total))

# $  python3 task4.py
# Kernel:System:Ticket:TicketPermission:  144
# Kernel::System::Ticket::TicketPermission: 8878
# Kernel::System::AuthSession::DB::CheckSessionID: 5756
# Kernel::System::Ticket::TicketLockSet: 2257
# Kernel::System::Ticket::TicketGet: 1015
# Kernel::System::DynamicField::Backend::ValueGet: 981
# Kernel::System::Ticket::TicketSubjectClean: 748
# Kernel::Modules::AgentTicketLock::Run: 742
# /opt/otrs/bin/otrs.ReprocessMails.pl: 717
# (eval): 716
# Kernel::System::User::GetUserData: 631
# Kernel::System::Ticket::Article::ArticleGet: 340
# Kernel::System::Queue::QueueStandardTemplateMemberList: 332
# Kernel::System::Ticket::TicketFlagGet: 331
# Kernel::System::Ticket::ArticleStorageFS::ArticleDeleteAttachment: 246
# Kernel::System::Web::UploadCache::FS::FormIDAddFile: 146
# Kernel::System::Priority::PriorityLookup: 83
# Kernel::System::Group::GroupUserRoleMemberList: 76
# Kernel::System::Web::InterfaceAgent::Run: 75
# Kernel::System::CustomerUser::GetPreferences: 72
# Kernel::System::Email::Sendmail::Send: 49
# Kernel::System::Ticket::TicketPrioritySet: 47
# Kernel::System::RegRu::ComplexityWork::SetPoints: 45
# Kernel::System::PostMaster::NewTicket::Run: 36
# Kernel::System::MailAccount::POP3::Fetch: 30
# Kernel::System::Email::Send: 14
# Kernel::System::Ticket::Article::ArticleSend: 14
# Kernel::System::Ticket::Event::ArticleAutoResponseFlagSet::Run: 14
# Kernel::System::Ticket::TicketGetOpen: 7
# Kernel::System::RTIndex::Do: 4
# Kernel::System::Ticket::ArticleStorageFS::_ArticleDeleteDirectory: 4
# Kernel::System::Time::WeWork: 3
# Kernel::System::Ticket::ArticleStorageFS::ArticleDeletePlain: 2
# Kernel::System::PDF::new: 2
# Kernel::System::Notification::SendSmsNotification: 2
# Kernel::System::Stats::GetObjectBehaviours: 2
# Kernel::System::Main::FileWrite: 2
# Kernel::System::Queue::GetQueueGroupID: 1
# Kernel::System::PostMaster::Reply::Run: 1
# Kernel::System::Ticket::TicketCreate: 1
# /opt/otrs/bin/otrs.PostMaster.pl: 1
# Kernel::Output::HTML::Layout::Error: 1