
Maid.rules do

  rule 'move 2019 journal files into folder' do
    move(dir('~/Dropbox/Journal/2019*.markdown'), '~/Dropbox/Journal/2019')
  end

  rule 'move Benefit Wallet files into folder' do
    move(dir('~/Scans/Benefit Wallet Receipt*.pdf'), '/home/wadeallen/Dropbox/Receipts/Medical/Benefit_Wallet')
  end

  rule 'move Thrivent Credit Union into folder' do
    move(dir('~/Scans/Thrivent Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Thrivent Credit Union')
  end

  rule 'move Paystubs into folder' do
    move(dir('~/Scans/*Paystub.pdf'), '/home/wadeallen/Dropbox/Paystubs')
  end

  rule 'move Ball State Credit Union into folder' do
    move(dir('~/Scans/Ball State Credit Union*.pdf'), '/home/wadeallen/Dropbox/Receipts/Ball State Credit Union')
  end

  rule 'move Hooser Healthwise into folder' do
    move(dir('~/Scans/Levi Hoosier Healthwise*.pdf'), '/home/wadeallen/Dropbox/Receipts/Insurance/Health Insurance/Hoosier Healthwise')
  end

  rule 'move Forum Credit Union into folder' do
    move(dir('~/Scans/Forum Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Forum Credit Union')
  end

  rule 'move Teachers Credit Union into folder' do
    move(dir('~/Scans/Teachers Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Teachers Credit Union')
  end

  rule 'move Evansville Teachers Credit Union into folder' do
    move(dir('~/Scans/Evansville Teachers Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Evansville Teachers Credit Union')
  end

  rule 'move Teachers Credit Union into folder' do
    move(dir('~/Scans/Teachers Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Teachers Credit Union')
  end

  rule 'move Three Rivers Credit Union into folder' do
    move(dir('~/Scans/Three Rivers Credit Union*.pdf'), '/home/wadeallen/Dropbox/Statements/Three Rivers Credit Union')
  end

  rule 'move reminder call sheets into folder' do
    move(dir('~/Scans/*Nursery Reminder Calls.pdf'), '~/Dropbox/Administration/Nursery/Reminder Calls')
  end

  rule 'move nursery sign in sheets into folder' do
    move(dir('~/Scans/*Nursery Worker Sign In Sheet.pdf'), '/home/wadeallen/Dropbox/Administration/Nursery/Sign In Sheets')
  end

  rule 'move Macys Statement into folder' do
    move(dir('~/Scans/Macys Statement*.pdf'), '~/Dropbox/Statements/Macys')
  end

  rule 'move giving reports into folder' do
    move(dir('~/Scans/*Giving Report.pdf'), '~/Dropbox/Administration/Giving Reports')
  end

  rule 'move benefit wallet receipts into folder' do
    move(dir('~/Scans/Benefit Wallet*.pdf'), '~/Dropbox/Receipts/Medical/Benefit Wallet Receipts')
  end

  rule 'move church receipts into folder' do
    move(dir('~/Scans/*Church Receipt*.pdf'), '~/Dropbox/Receipts/Church/Current')
  end

  rule 'move housing receipts into folder' do
    move(dir('~/Scans/*Housing Receipt*.pdf'), '~/Dropbox/Receipts/Housing/Misc Housing')
  end

  rule 'move Comcast Bill into folder' do
    move(dir('~/Desktop/Comcast Bill*.pdf'), '~/Dropbox/Receipts/Housing/Comcast')
  end

  rule 'move Kohls Statement into folder' do
    move(dir('~/Scans/Kohls Statement*.pdf'), '~/Dropbox/Statements/Kohls')
  end

  rule 'move American Eagle Statement into folder' do
    move(dir('~/Scans/American Eagle Statement*.pdf'), '~/Dropbox/Statements/American Eagle')
  end

  rule 'move Indiana Michigan Power Statement into folder' do
    move(dir('~/Scans/I&MBill_*.pdf'), '~/Dropbox/Receipts/Housing/Utilities/Electric')

  rule 'move School Receipts into folder' do
    move(dir('~/Scans/*School Receipt*.pdf'), '~/Dropbox/Receipts/School')
  end

  rule 'move Yorktown Muncipal Utilities into folder' do
    move(dir('~/Scans/Yorktown Municipal Utilities*.pdf'), '~/Dropbox/Receipts/Housing/Utilities/Water')
  end

  rule 'move Maurices Statement into folder' do
    move(dir('~/Scans/Maurices*.pdf'), '~/Dropbox/Statements/Maurices')
  end

  rule 'move Target Statement into folder' do
    move(dir('~/Scans/Target Card*.pdf'), '~/Dropbox/Receipts/Target')
  end

  rule 'move Anna Vanderbilt Health Insurance Statement into folder' do
    move(dir('~/Scans/Anna Vanderbilt Health Insurance*.pdf'), '~/Dropbox/Anna/Anna_Vanderbilt')
  end

  rule 'move New York and Company Statement into folder' do
    move(dir('~/Scans/New York and Company*.pdf'), '~/Dropbox/Receipts/New York and Company')
  end

  rule 'move TJ Maxx Statement into folder' do
    move(dir('~/Scans/TJ Maxx Statement*.pdf'), '~/Dropbox/Receipts/TJ Maxx')
  end

  rule 'move Victoria Secret Statement into folder' do
    move(dir('~/Scans/Victoria Secret Statement*.pdf'), '~/Dropbox/Receipts/Victoria Secret')
  end

  rule 'move Childrens Place Statement into folder' do
    move(dir('~/Scans/Childrens Place Statement*.pdf'), '~/Dropbox/Receipts/Childrens Place')
  end

  rule 'move ATT Statement into folder' do
    move(dir('~/Desktop/ATT_Bill_*.pdf'), '~/Dropbox/Receipts/Wireless Phone')
  end

  rule 'move IU Health Statement into folder' do
    move(dir('~/Scans/IU Health Insurance*.pdf'), '~/Dropbox/Receipts/Insurance/Health Insurance/IU Health Insurance')
  end

  rule 'move CareSource Statement into folder' do
    move(dir('~/Scans/CareSource*.pdf'), '~/Dropbox/Receipts/Insurance/CareSource')
  end

  rule 'move MD Wise Statement into folder' do
    move(dir('~/Scans/MD Wise*.pdf'), '~/Dropbox/Receipts/Insurance/Health Insurance/MD Wise Wade Christy')
  end

  rule 'move Vectren Bill into folder' do
    move(dir('~/Scans/Vectren*.pdf'), '~/Dropbox/Receipts/Housing/Utilities/Gas')
  end

  end
end


